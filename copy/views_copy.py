# from typing import Any
# from .models import Faculty, Group, Teacher, Lesson, Student, Mark, Hometask
# from .serializers import *
# from rest_framework import viewsets
# from django.db import models
# from django.shortcuts import render
# from django.views.generic import ListView
# from django.core.paginator import Paginator
# from . import config
# from rest_framework import permissions, viewsets, parsers, status as status_codes
# from rest_framework.response import Response
# from django.db import models, transaction
# from .forms import AddMarkForm
# from django.contrib.auth import decorators as auth_decorators, mixins as auth_mixins
# from django.http import HttpResponseRedirect
# from django.urls import reverse



# @auth_decorators.login_required
# def profile_page(request):
#     user = request.user
#     user_data = {
#         'Username': user.username,
#         'First name': user.first_name,
#         'Last name': user.last_name,
#         'Email': user.email,
#     }
#     return render(
#         request,
#         config.TEMPLATE_PROFILE,
#         context={
#             'user_data': user_data,
#         },
#     )


# def custom_main(req):
#     return render(
#         req,
#         config.TEMPLATE_MAIN,
#         context={
#             'faculties': Faculty.objects.all().count(),
#             'groups': Group.objects.all().count(),
#             'teachers': Teacher.objects.all().count(),
#             'students': Student.objects.all().count(),
#         },
#     )


# def student_objects(student, cls_model):
#     if cls_model is Group:
#         return student.group      # но так работать не будет
#     elif cls_model is Lesson:
#         return Lesson.objects.filter()    # непонятно как делать
#     elif cls_model is Mark:
#         return Mark.objects.filter(student=student)
#     elif cls_model is Hometask:
#         return Hometask.objects.filter()  # непонятно как делать

# def catalog_view(cls_model: models.Model, page_name, template):
#     class CustomListView(ListView):     # auth_mixins.LoginRequiredMixin, 
#         # LoginRequiredMixin - Verify that the current user is authenticated.
#         model = cls_model
#         template_name = template
#         context_object_name = page_name

#         def get_context_data(self, request, **kwargs: Any):
#             order_key = {
#                 'faculties': 'title',
#                 'groups': 'title',
#                 'teachers': 'full_name',
#                 'lessons': 'day',
#                 'marks': 'created',     # надо lesson.day
#                 'hometasks': 'task'
#             }
#             # это получается то же самое что внизу в entity_view, может как-то по-другому сделать можно FIXME
#             # if user is student:                         # TODO получить user
#             context = super().get_context_data(**kwargs)
#             user = request.user                      # HACK
#             student = Student.objects.get(user=user)
#             instances = cls_model.objects.order_by(order_key[page_name])
#             if student:
#                 instances = student_objects(student, cls_model).order_by(order_key[page_name])
#             # if user is teacher:
#             else:
#                 teacher = Teacher.objects.get(user=user)
#                 if cls_model is Group:
#                     instances = Group.objects.order_by(order_key[page_name]).filter()
#                 elif cls_model is Lesson:
#                     instances = Lesson.objects.order_by(order_key[page_name]).filter(teacher=teacher)
#                 elif cls_model is Mark:
#                     instances = Mark.objects.order_by(order_key[page_name]).filter(lesson__in=Lesson.objects.filter(teacher=teacher))
#                 elif cls_model is Hometask:
#                     instances = Hometask.objects.order_by(order_key[page_name]).filter()
#             paginator = Paginator(instances, config.PAGINATE_THRESHOLD)
#             page_number = self.request.GET.get('page')
#             page_obj = paginator.get_page(page_number)
#             context[f'{page_name}_list'] = page_obj
#             return context
#     return CustomListView


# FacultyListView = catalog_view(Faculty, 'faculties', config.FACULTIES_CATALOG)
# TeacherListView = catalog_view(Teacher, 'teachers', config.TEACHERS_CATALOG)

# GroupListView = catalog_view(Group, 'groups', config.GROUPS_CATALOG)
# LessonListView = catalog_view(Lesson, 'lessons', config.LESSONS_CATALOG)
# MarkListView = catalog_view(Mark, 'marks', config.MARKS_CATALOG)
# HometaskListView = catalog_view(Hometask, 'hometasks', config.HOMETASKS_CATALOG)


# def entity_view(cls_model, name, template):
#     # @auth_decorators.login_required       # это тут мешает, учителей же всем смотреть можно  
#     # Decorator for views that checks that the user is logged in, redirecting to the log-in page if necessary.
#     def view(request):
#         target_obj = cls_model.objects.get(id=request.GET.get('id', ''))
#         context = {name: target_obj}
#         to_render = [request, template]

#         if cls_model in (Lesson, Mark, Group, Hometask):
#             user = request.user
#             student = Student.objects.get(user=user)
#             if student:
#                 instances = student_objects(student, cls_model)
#                 marks = Mark.objects.filter(student=student)
#                 # lessons = []
#                 # for lesson in Lesson.objects.all():
#                 #     if student.group in lesson.groups:
#                 #         lessons.append(lesson)
#                 lessons = Lesson.objects.all()     # student.group in lesson.groups   TODO
#                 groups = student.group      # но так работать не будет       
#                 hometasks = Hometask.objects.all(lesson__in=lessons)          # HACK
#                 # Lesson.objects.filter(subject__in=student.group.subjects)    # это не работает
#             else:
#                 teacher = Teacher.objects.get(user=user)
#                 if request.method == 'POST':        # надо сделать, чтобы это работало только для mark
#                     form = AddMarkForm(request.POST)
#                     if form.is_valid():
#                         fields = ['mark', 'presence', 'student', 'lesson']
#                         data_to_add = [form.cleaned_data.get(field) for field in fields]
#                         with transaction.atomic():
#                             Mark.objects.create(**data_to_add)
#                             teacher.save()       # а как
#                         return HttpResponseRedirect(reverse('mark'))
#                     context['form'] =  AddMarkForm()     # а это так надо?
#                     context['form_errors'] = form.errors 
#                 marks = Mark.objects.filter(lesson__in=Lesson.objects.filter(teacher=teacher))
#                 lessons = Lesson.objects.filter(teacher=teacher)
#                 #groups = Group.objects.filter(subjects=teacher.subjects)
#                 groups = Group.objects.all()            # TODO
#             # if cls_model is Lesson:
#             #     context[f'user_{cls_model}'.lower()] = target_obj in instances
#             # if cls_model is Mark:
#             #     context[f'user_{cls_model}'.lower()] = target_obj in instances
#             # if cls_model is Group:
#             context[f'user_{cls_model}'.lower()] = target_obj in instances

#         return render(*to_render, context=context)
#     return view



# faculty_view = entity_view(Faculty, 'faculty', config.FACULTY_ENTITY)
# group_view = entity_view(Group, 'group', config.GROUP_ENTITY)
# teacher_view = entity_view(Teacher, 'teacher', config.TEACHER_ENTITY)
# lesson_view = entity_view(Lesson, 'lesson', config.LESSON_ENTITY)
# mark_view = entity_view(Mark, 'mark', config.MARK_ENTITY)
# hometask_view = entity_view(Hometask, 'hometask', config.HOMETASK_ENTITY)



# class Permission(permissions.BasePermission):
#     def has_permission(self, request, _):
#         if request.method in config.SAFE_METHODS:
#             return bool(request.user and request.user.is_authenticated)
#         elif request.method in config.UNSAFE_METHODS:
#             return bool(request.user and request.user.is_superuser)
#         return False


# def query_from_request(request, cls_serializer=None) -> dict:
#     if cls_serializer:
#         query = {}
#         for attr in cls_serializer.Meta.fields:
#             attr_value = request.GET.get(attr, '')
#             if attr_value:
#                 query[attr] = attr_value
#         return query
#     return request.GET


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
#                 instances = cls_model.objects.filter(**query)
#                 objects_num = len(instances)
#                 if not objects_num:
#                     msg = f'DELETE query {query} did not match any instances of {cls_model.__name__}'
#                     return Response(msg, status=status_codes.HTTP_404_NOT_FOUND)
#                 try:
#                     instances.delete()
#                 except Exception as error:
#                     return Response(error, status=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)
#                 msg = f'DELETED {objects_num} instances of {cls_model.__name__}'
#                 status = status_codes.HTTP_204_NO_CONTENT if objects_num == 1 else status_codes.HTTP_200_OK
#                 return Response(msg, status=status)
#             return Response('DELETE has got no query', status=status_codes.HTTP_400_BAD_REQUEST)

#         def put(self, request):
#             def serialize(target):
#                 payload = parsers.JSONParser().parse(request)
#                 if target:
#                     serialized = serializer(target, data=payload, partial=True)
#                     status = status_codes.HTTP_200_OK
#                     body = f'PUT has updated instance of {cls_model.__name__} id={target.id}'
#                 else:
#                     serialized = serializer(data=payload, partial=True)
#                     status = status_codes.HTTP_201_CREATED
#                     body = f'PUT has created a new instance of {cls_model.__name__}'

#                 if not serialized.is_valid():
#                     return status_codes.HTTP_400_BAD_REQUEST, f'PUT could not process content: {payload}'

#                 try:
#                     serialized.save()
#                 except Exception as error:
#                     return status_codes.HTTP_500_INTERNAL_SERVER_ERROR, error
#                 return status, body

#             query = query_from_request(request, serializer)
#             target_id = query.get('id', '')
#             if target_id:
#                 target_object = cls_model.objects.get(id=target_id)
#                 status, body = serialize(target_object)
#                 return Response(body, status=status)
#             return Response('PUT has got no id primary key', status=status_codes.HTTP_400_BAD_REQUEST)

#     return CustomViewSet



# FacultyViewSet = create_viewset(Faculty, FacultySerializer, 'title')
# TeacherViewSet = create_viewset(Teacher, TeacherSerializer, 'full_name')
# LessonViewSet = create_viewset(Lesson, LessonSerializer, 'day')
# MarkViewSet = create_viewset(Mark, MarkSerializer, 'created')  # хочу lesson.day указать
# HometaskViewSet = create_viewset(Hometask, HometaskSerializer, 'task')
# GroupViewSet = create_viewset(Group, GroupSerializer, 'title')



# # но change_password тоже надо сделать конечно. Потом.

# # надо делать отдельно завуча (который не студент и не учитель)?

# # неавторизованные должны видеть факультеты и учителей
# # где-то он перебрасывает на логин, если ты не авторизован

# # TODO - когда-нибудь сделать
# # FIXME - на чем я остановилась
# # HACK - может не работать
# # NOTE 