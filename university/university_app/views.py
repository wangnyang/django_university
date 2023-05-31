from typing import Any
from .models import Faculty, Group, Teacher, Lesson, Student, Mark, Hometask
from .serializers import *
from rest_framework import viewsets
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from . import config
from rest_framework import permissions, viewsets, parsers, status as status_codes
from rest_framework.response import Response
from django.db import models, transaction
from .forms import AddMarkForm
from django.contrib.auth import decorators as auth_decorators, mixins as auth_mixins
from django.http import HttpResponseRedirect
from django.urls import reverse


@auth_decorators.login_required
def profile_page(request):
    user = request.user
    user_data = {
        'Username': user.username,
        'First name': user.first_name,
        'Last name': user.last_name,
        'Email': user.email,
    }
    return render(
        request,
        config.TEMPLATE_PROFILE,
        context={
            'user_data': user_data,
        },
    )


def custom_main(req):
    return render(
        req,
        config.TEMPLATE_MAIN,
        context={
            'faculties': Faculty.objects.all().count(),
            'groups': Group.objects.all().count(),
            'teachers': Teacher.objects.all().count(),
            'students': Student.objects.all().count(),
        },
    )


def student_objects(student: Student, cls_model: models.Model):
    lessons = []
    for lesson in Lesson.objects.all():
        if student.group in lesson.groups.all():
            lessons.append(lesson)
    if cls_model is Group:
        return [student.group,]
    elif cls_model is Lesson:
        return lessons
    elif cls_model is Mark:
        return Mark.objects.filter(student=student)
    elif cls_model is Hometask:
        return Hometask.objects.filter(lesson__in=lessons)
    return cls_model.objects.all()


def teacher_objects(teacher: Teacher, cls_model: models.Model):
    lessons = Lesson.objects.filter(teacher=teacher)
    if cls_model is Group:
        groups = []
        for group in Group.objects.all():
            for subject in group.subjects.all():
                if subject in teacher.subjects.all():
                    groups.append(group)
        return groups
    elif cls_model is Lesson:
        return lessons
    elif cls_model is Mark:
        return Mark.objects.filter(lesson__in=Lesson.objects.filter(teacher=teacher))
    elif cls_model is Hometask:
        return Hometask.objects.filter(lesson__in=lessons)
    return cls_model.objects.all()


def get_objects_for_user(request, cls_model):
    user = request.user
    if user.is_superuser:
        return cls_model.objects.all()
    try:
        student = Student.objects.get(user=user)
    except Exception:
        student = None
    if student:
        return student_objects(student, cls_model)
    try:
        teacher = Teacher.objects.get(user=user)
    except Exception:
        teacher = None
    if teacher:
        return teacher_objects(teacher, cls_model)
    if cls_model in (Faculty, Teacher):
        return cls_model.objects.all()
    return []


def catalog_view(cls_model: models.Model, page_name, template):
    class CustomListView(ListView):
        model = cls_model
        template_name = template
        context_object_name = page_name

        def get_context_data(self, **kwargs: Any):
            context = super().get_context_data(**kwargs)
            instances = get_objects_for_user(self.request, cls_model)
            context[f'{page_name}_list'] = instances
            return context
    return CustomListView


FacultyListView = catalog_view(Faculty, 'faculties', config.FACULTIES_CATALOG)
TeacherListView = catalog_view(Teacher, 'teachers', config.TEACHERS_CATALOG)

GroupListView = catalog_view(Group, 'groups', config.GROUPS_CATALOG)
LessonListView = catalog_view(Lesson, 'lessons', config.LESSONS_CATALOG)
MarkListView = catalog_view(Mark, 'marks', config.MARKS_CATALOG)
HometaskListView = catalog_view(Hometask, 'hometasks', config.HOMETASKS_CATALOG)


def entity_view(cls_model, name, template):
    def view(request):
        target_obj = cls_model.objects.get(id=request.GET.get('id', ''))
        context = {name: target_obj}
        to_render = [request, template]

        instances = get_objects_for_user(request, cls_model)
        context[f'user_{cls_model}'.lower()] = target_obj in instances

        if cls_model is Lesson:
            if request.method == "POST":
                form = AddMarkForm(target_obj, request.POST)      
                # AddMarkForm.__init__() takes 2 positional arguments but 3 were given
                if form.is_valid():
                    form.save()
                    return redirect('lessons')
            else:
                form = AddMarkForm(target_obj)
                context['form']= form
                context['lesson'] = target_obj
                context['form_errors'] = form.errors
        return render(*to_render, context=context)
    return view


# у одного урока два раза одна и та же группа перечислена TODO


faculty_view = entity_view(Faculty, 'faculty', config.FACULTY_ENTITY)
group_view = entity_view(Group, 'group', config.GROUP_ENTITY)
teacher_view = entity_view(Teacher, 'teacher', config.TEACHER_ENTITY)
lesson_view = entity_view(Lesson, 'lesson', config.LESSON_ENTITY)
mark_view = entity_view(Mark, 'mark', config.MARK_ENTITY)
hometask_view = entity_view(Hometask, 'hometask', config.HOMETASK_ENTITY)


class Permission(permissions.BasePermission):
    def has_permission(self, request, _):
        if request.method in config.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        elif request.method in config.UNSAFE_METHODS:
            # teacher = Teacher.objects.get(user=request.user)
            return bool(request.user and (request.user.is_superuser))       # TODO teacher or superuser
        return False


def query_from_request(request, serializer=None):
    if serializer:
        query = {}
        for attr in serializer.Meta.fields:
            attr_value = request.GET.get(attr, '')
            if attr_value:
                query[attr] = attr_value
        return query
    return request.GET



# def create_viewset(cls_model: models.Model, serializer, order_field):
#     class CustomViewSet(viewsets.ModelViewSet):
#         serializer_class = serializer
#         queryset = cls_model.objects.all().order_by(order_field)
#         permission_classes = [Permission]

#         def get_queryset(self):
#             instances = cls_model.objects.all()
#             query = query_from_request(self.request, serializer)
#             if query:
#                 instances = instances.filter(**query)
#             return instances.order_by(order_field)
        
#         def delete(self, request):
#             query = query_from_request(request, serializer)
#             if query:
#                 instances = cls_model.filter(**query)
#                 instances_num = len(instances)
#                 if not instances_num:
#                     message = f'DELETE query {query} did not match any {cls_model.__name__} instances'
#                     return Response(message, status=status_codes.HTTP_404_NOT_FOUND)
#                 try:
#                     instances.delete()
#                 except Exception as error:
#                     return Response(error, status=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)
#                 message = f'Deleted {instances_num} {cls_model.__name__} instances'
#                 status_code = status_codes.HTTP_204_NO_CONTENT if instances_num == 1 else status_codes.HTTP_200_OK
#                 return Response(message, status_code)
#             return Response('DELETE has got no query', status=status_codes.HTTP_400_BAD_REQUEST)

#         def put(self, request):
#             def serialize(target):
#                 payload = parsers.JSONParser().parse(request)
#                 if target:
#                     serialized = serializer(target, data=payload, partial=True)
#                     status_code = status_codes.HTTP_200_OK
#                     message = f'PUT has updated {cls_model.__name__} with id={target.id}'
#                 else: # POST
#                     serialized = serializer(data=payload, partial=True)
#                     status_code = status_codes.HTTP_201_CREATED
#                     message = f'PUT has created a new {cls_model.__name__} instance'
#                 if not serialized.is_valid():
#                     return status_codes.HTTP_400_BAD_REQUEST, f'PUT could not process data {payload}'
                
#                 try:
#                     serialized.save()
#                 except Exception as error:
#                     return status_codes.HTTP_500_INTERNAL_SERVER_ERROR, error
                
#                 return status_code, message
#             query = query_from_request(request, serializer)
#             instance_id = query.get('id', '')
#             if instance_id:
#                 instance = cls_model.objects.get(id=instance_id)
#                 status_code, message = serialize(instance)
#                 return Response(message, status_code)
#             return Response('PUT has got no id', status_codes.HTTP_400_BAD_REQUEST)
        
#     return CustomViewSet


def create_viewset(cls_model: models.Model, serializer, permission, order_field):
    class_name = f"{cls_model.__name__}ViewSet"
    doc = f"API endpoint that allows users to be viewed or edited for {cls_model.__name__}"
    CustomViewSet = type(class_name, (viewsets.ModelViewSet,), {
        "doc": doc,
        "serializer_class": serializer,
        "queryset": cls_model.objects.all().order_by(order_field),
        "permission_classes": [permission],
        "get_queryset": lambda self, *args, **kwargs:
              cls_model.objects.filter(**query_from_request(self.request, serializer)).order_by(order_field),
    })
    return CustomViewSet


# ViewSet class automatically creates functions list(), create(), retrieve(), update(), destroy()


FacultyViewSet = create_viewset(Faculty, FacultySerializer, Permission, 'title')
TeacherViewSet = create_viewset(Teacher, TeacherSerializer, Permission, 'full_name')
LessonViewSet = create_viewset(Lesson, LessonSerializer, Permission, 'day')
MarkViewSet = create_viewset(Mark, MarkSerializer, Permission, 'created')        # хочу lesson.day указать
HometaskViewSet = create_viewset(Hometask, HometaskSerializer, Permission, 'task')
GroupViewSet = create_viewset(Group, GroupSerializer, Permission, 'title')

