from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.test.client import Client
from university_app.models import Faculty, Group, Subject, Teacher, Lesson, Student, Mark, Hometask
from rest_framework import status
from rest_framework.test import APIClient
import json
from . import attrs

# сами запускаются только те функции, которые начинаются на test_


def create_viewset_tests(url, cls_model, request_content, to_change):  
    # request content - data for POST
    # to_change - data for PUT
    class ViewSetTests(TestCase):

        def setUp(self):
            self.client = Client()      # Client - a class that can act as a client for testing purposes.
            self.creds_user = {'username': 'user', 'password': 'user'}
            self.creds_superuser = {'username': 'superuser', 'password': 'superuser'}
            self.user = User.objects.create_user(**self.creds_user)
            self.superuser = User.objects.create_user(is_superuser=True, **self.creds_superuser)
            self.token = Token.objects.create(user=self.superuser)

        def test_get(self):     # logging in with user and opening the site, must be 200 OK
            self.client.login(**self.creds_user)
            resp_get = self.client.get(url)
            self.assertEqual(resp_get.status_code, status.HTTP_200_OK)

            # logging out
            self.client.logout()

        def manage(self, headers=None):
            # POST
            resp_post = self.client.post(url, data=request_content, headers=headers)
            self.assertEqual(resp_post.status_code, status.HTTP_201_CREATED)

            # PUT
            created = cls_model.objects.get(**request_content)      # get the data created in POST
            url_to_created = f'{url}?id={created.id}'
            resp_put = self.client.put(url_to_created, data=json.dumps(to_change), headers=headers)
            self.assertEqual(resp_put.status_code, status.HTTP_200_OK)
            attr, attr_value = list(to_change.items())[0]
            after_put = cls_model.objects.get(id=created.id)        # get the data that was changed
            self.assertEqual(getattr(after_put, attr), attr_value)  # check that this attr value in this object = attr_value from query

            # DELETE EXISTING
            resp_delete = self.client.delete(url_to_created)
            self.assertEqual(resp_delete.status_code, status.HTTP_204_NO_CONTENT)

            # DELETE NONEXISTENT
            resp_delete = self.client.delete(url_to_created)       # we already deleted this data
            self.assertEqual(resp_delete.status_code, status.HTTP_404_NOT_FOUND)

        def test_manage_superuser(self):
            # logging in with user
            self.client.login(**self.creds_superuser)

            self.manage()

            # logging out
            self.client.logout()

        def test_manage_token(self):
            # logging in with rest_framework APIClient
            # (it can be forcefully authenticated with token)
            self.client = APIClient()

            # token goes brrr
            self.client.force_authenticate(user=self.superuser, token=self.token)

        def test_manage_user(self):     # testing that normal users cannot send POST, PUT or DELETE
            # logging in with user
            self.client.login(**self.creds_user)

            # POST
            resp_post = self.client.post(url, data=request_content)
            self.assertEqual(resp_post.status_code, status.HTTP_403_FORBIDDEN)

            # PUT
            created = cls_model.objects.create(**request_content)
            url_to_created = f'{url}?id={created.id}'
            resp_put = self.client.put(url_to_created, data=json.dumps(to_change))
            self.assertEqual(resp_put.status_code, status.HTTP_403_FORBIDDEN)

            # DELETE EXISTING
            resp_delete = self.client.delete(url_to_created)
            self.assertEqual(resp_delete.status_code, status.HTTP_403_FORBIDDEN)

            # clean up
            created.delete()

            # logging out
            self.client.logout()
    return ViewSetTests


# request content - data for POST
# to_change - data for PUT
class_objects = attrs.setUp()


FacultyViewSetTests = create_viewset_tests('/rest/faculty/', Faculty, attrs.faculty_attrs, {'description': 'new description'})
GroupViewSetTests = create_viewset_tests('/rest/faculty/', Group, attrs.group_attrs, {'title': attrs.some_text})
SubjectViewSetTests = create_viewset_tests('/rest/faculty/', Subject, attrs.subject_attrs, {'title': attrs.some_text})
TeacherViewSetTests = create_viewset_tests('/rest/faculty/', Teacher, attrs.teacher_attrs, {'full_name': attrs.some_text})
LessonViewSetTests = create_viewset_tests('/rest/faculty/', Lesson, attrs.lesson_attrs, {'day': '2023-05-30'})
StudentViewSetTests = create_viewset_tests('/rest/faculty/', Student, attrs.student_attrs, {'full_name': attrs.some_text})
MarkViewSetTests = create_viewset_tests('/rest/faculty/', Mark, attrs.mark_attrs, {'mark': 5})
HometaskViewSetTests = create_viewset_tests('/rest/faculty/', Hometask, attrs.hometask_attrs, {'task': 'new task'})
