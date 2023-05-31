from university_app.models import Faculty, Group, Subject, Teacher, Lesson, Student
from university_app.config import CHARS_DEFAULT
from random import sample, randint, choice
from string import ascii_letters

def setUp():
    class_objects = {}
    faculty = {'title': 'Linguistics'}
    fc = Faculty.objects.create(**faculty)
    fc.save()
    class_objects['faculty'] = fc
    subject = {'title': 'English'}
    su = Subject.objects.create(**subject)
    su.save()
    class_objects['subject'] = su
    teacher = {'full_name': 'Dennis Keller', 'faculty': fc}
    te = Teacher.objects.create(**teacher)
    te.save()
    class_objects['teacher'] = te
    lesson  = {'day': '2023-04-07', 'precise_time': '14:45:00', 'subject': su, 'teacher': te}
    le =  Lesson.objects.create(**lesson)
    le.save()
    class_objects['lesson'] = le
    group = {'title': '7.1', 'faculty': fc}
    gr = Group.objects.create(**group)
    gr.save()
    class_objects['group'] = gr
    student = {'full_name': 'Steven Wright', 'group': gr}
    st = Student.objects.create(**student)
    st.save()
    class_objects['student'] = st
    return class_objects


class_objects = setUp()

# normal and failing attrs
normal_title = ''.join(sample(ascii_letters, CHARS_DEFAULT - 1))
failing_title = ''.join(sample(ascii_letters, CHARS_DEFAULT + 1))
some_text = ''.join(sample(ascii_letters, CHARS_DEFAULT - 1))
normal_mark = choice([randint(1, 5), None])     #
normal_presence = choice(['Н', None])     #
failing_mark = choice([-1, 6])      # как ли нужно делать, или брать просто значение?
failing_presence = choice(ascii_letters)


# dictionaries with attrs
subject_attrs = {'title': normal_title}
subject_failing_attrs = {'title': failing_title}

student_attrs = {'full_name': normal_title}
student_failing_attrs = {'full_name': failing_title}

teacher_attrs = {'full_name': normal_title, 'faculty': class_objects['faculty']}
teacher_failing_attrs = {'full_name': failing_title, 'faculty': class_objects['faculty']}

faculty_attrs = {'title': normal_title, 'description': some_text}
faculty_failing_attrs = {'title': failing_title, 'description': some_text}

lesson_attrs = {'day': '2023-12-31', 'precise_time': '09:45:00', 'subject': class_objects['subject'], 'teacher': class_objects['teacher']}
lesson_failing_attrs = {'day': '2023-13-40', 'time': '24:70:61', 'subject': class_objects['subject'], 'teacher': class_objects['teacher']}

mark_attrs = {'mark': normal_mark, 'presence': normal_presence, 'lesson': class_objects['lesson'], 'student': class_objects['student']}
mark_failing_attrs = {'mark': failing_mark, 'presence': failing_presence}

group_attrs = {'title': normal_title, 'faculty': class_objects['faculty']}
group_failing_attrs = {'title': failing_title, 'faculty': class_objects['faculty']}

hometask_attrs = {'task': some_text, 'lesson': class_objects['lesson']}
hometask_failing_attrs = {'task': '', 'lesson': class_objects['lesson']}


# а если все тесты запускать, в test_models будут создаваться эти объекты, а потом в test_views? Плохо
