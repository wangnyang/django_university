from .models import Faculty, Group, Teacher, Lesson, Mark, Hometask, Subject, Student
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField


class FacultySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Faculty
        fields = ('id', 'title', 'description')


class GroupSerializer(HyperlinkedModelSerializer):      # v
    faculty = PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    lessons = PrimaryKeyRelatedField(queryset=Lesson.objects.all(), many=True)
    subjects = PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'faculty', 'lessons', 'subjects')


class TeacherSerializer(HyperlinkedModelSerializer):
    subjects = PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True)
    faculty = PrimaryKeyRelatedField(queryset=Faculty.objects.all())

    class Meta:
        model = Teacher
        fields = ('id', 'full_name', 'subjects', 'faculty')


class LessonSerializer(HyperlinkedModelSerializer):     # v
    subject = PrimaryKeyRelatedField(queryset=Subject.objects.all())
    teacher = PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    groups = PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    class Meta:
        model = Lesson
        fields = ('id', 'day', 'precise_time', 'subject', 'teacher', 'groups')


class MarkSerializer(HyperlinkedModelSerializer):   # v
    student = PrimaryKeyRelatedField(queryset=Student.objects.all())
    lesson = PrimaryKeyRelatedField(queryset=Lesson.objects.all())

    class Meta:
        model = Mark
        fields = ('id', 'mark', 'presence', 'created', 'modified', 'student', 'lesson')


class HometaskSerializer(HyperlinkedModelSerializer):
    lesson = PrimaryKeyRelatedField(queryset=Lesson.objects.all())

    class Meta:
        model = Hometask
        fields = ('id', 'task', 'created', 'lesson')


# is it OK that validators don't work?
