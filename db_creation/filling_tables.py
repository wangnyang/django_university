from faker import Faker
import psycopg2
from dotenv import load_dotenv
from os import getenv
from random import choice, randint
from faculties_dict import faculties

load_dotenv()
PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')


db_connection = psycopg2.connect(dbname=PG_DBNAME, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)
db_cursor = db_connection.cursor()

faker = Faker()

# заполняем таблицу teacher:
# for _ in range(15):
#     db_cursor.execute('INSERT INTO teacher (full_name) values (%s)', (faker.name(),))
# db_cursor.execute('select * from teacher;')
# print(db_cursor.fetchall())
# db_connection.commit()


# # Добавляем факультеты и их описания в таблицу faculty
# for faculty, description in faculties.items():
#     db_cursor.execute('INSERT INTO faculty (title, description) VALUES (%s, %s)', (faculty, description))
# db_connection.commit()
# db_cursor.execute('SELECT id from faculty')
# faculty_ids = [i[0] for i in db_cursor.fetchall()]
# # print(faculty_ids)


# заполняем таблицу class:
# for year in range(5):
#     for group in range(randint(1, 5)):
#         title = f'{year}.{group}'
#         faculty_id = choice(faculty_ids)
#         db_cursor.execute('INSERT INTO class (title, faculty_id) VALUES (%s, %s)', (title, faculty_id))
# db_connection.commit()
db_cursor.execute('SELECT id from class')
class_ids = [i[0] for i in db_cursor.fetchall()]
# print(class_ids)


# заполняем таблицу subject_to_teacher (связями между subject_id и teacher_id)
# db_cursor.execute('select id from subject')
# subject_ids = [i[0] for i in db_cursor.fetchall()]
# db_cursor.execute('select id from teacher')
# teacher_ids = [i[0] for i in db_cursor.fetchall()]

# have_subjects = set()
# for subject_id in subject_ids:
#     teacher_id = choice(teacher_ids)
#     have_subjects.add(teacher_id)
#     db_cursor.execute('INSERT INTO subject_to_teacher (subject_id, teacher_id) VALUES (%s, %s)', (subject_id, teacher_id))
# for teacher_id in set(teacher_ids) - have_subjects:
#     subject_id = choice(subject_ids)
#     db_cursor.execute('INSERT INTO subject_to_teacher (subject_id, teacher_id) VALUES (%s, %s)', (subject_id, teacher_id))

# db_connection.commit()

# # смотрим, остались ли предметы без учителей
# db_cursor.execute('select id from subject where id not in (select subject_id from subject_to_teacher);')
# print(db_cursor.fetchall())


# заполняем таблицу student:
# for _ in range(200):
#     db_cursor.execute('INSERT INTO student (full_name, class_id) values (%s, %s)', (faker.name(), choice(class_ids)))
# db_connection.commit()
db_cursor.execute('select id from student;')
student_ids = db_cursor.fetchall()
db_cursor.execute('select id from lesson;')
lesson_ids = db_cursor.fetchall()

# заполняем mark:
# marks = [1, 2, 3, 4, 5, 'Н']
# for i in range(20):
#     student_id = choice(student_ids)
#     lesson_id = choice(lesson_ids)
#     mark = choice(marks)
#     if mark == 'Н':
#         db_cursor.execute('INSERT INTO mark (presence, student_id, lesson_id) values (%s, %s, %s)', (mark, student_id, lesson_id))
#     else:
#         db_cursor.execute('INSERT INTO mark (mark, student_id, lesson_id) values (%s, %s, %s)', (mark, student_id, lesson_id))
# db_connection.commit()

# hometask
"""
task text not null,
lesson_id uuid not null REFERENCES lesson
"""
tasks = ['Studentsbook page 5 exercise 1', 'Studentsbook page 95 exercise 4', 'Studentsbook pages 67-78',
         'Studentsbook paragraph 6', 'Studentsbook exercises 1, 2']
for i in range(20):
    lesson_id = choice(lesson_ids)
    task = choice(tasks)
    db_cursor.execute('INSERT INTO hometask (task, lesson_id) values (%s, %s)', (task, lesson_id))
db_connection.commit()


db_cursor.close()
db_connection.close()
