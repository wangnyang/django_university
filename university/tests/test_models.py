from django.test import TestCase
from university_app.models import Faculty, Group, Subject, Teacher, Lesson, Student, Mark, Hometask
from .attrs import *
from django.db.utils import DataError


class_objects = setUp()

def create_model_tests(cls_model, attrs, failing_attrs):
    class ModelTests(TestCase):

        def test_successful_creation(self):
            cls_model.objects.create(**attrs)
            for k, v in attrs.items():
                if isinstance(v, Faculty):
                    print(f'{cls_model.__name__} ATTR {k}: {v.__dict__}')

        def test_failing_creation(self):
            with self.assertRaises(DataError):
                cls_model.objects.create(**failing_attrs)

    return ModelTests


# tests creation (all attrs are located in attrs.py)
FacultyTests = create_model_tests(Faculty, faculty_attrs, faculty_failing_attrs)
GroupTests = create_model_tests(Group, group_attrs, group_failing_attrs)      # faculty_id
SubjectTests = create_model_tests(Subject, subject_attrs, subject_failing_attrs)
TeacherTests = create_model_tests(Teacher, teacher_attrs, teacher_failing_attrs)      # faculty_id
LessonTests = create_model_tests(Lesson, lesson_attrs, lesson_failing_attrs)      # subject_id, teacher_id
StudentTests = create_model_tests(Student, student_attrs, student_failing_attrs)
MarkTests = create_model_tests(Mark, mark_attrs, mark_failing_attrs)      # lesson_id, (student_id??)
HometaskTests = create_model_tests(Hometask, hometask_attrs, hometask_failing_attrs)       # lesson_id


# TODO should fail because of validators