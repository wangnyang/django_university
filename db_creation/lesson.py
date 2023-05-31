import psycopg2
from dotenv import load_dotenv
from os import getenv
from random import choice, randint

load_dotenv()
PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')


db_connection = psycopg2.connect(dbname=PG_DBNAME, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)
db_cursor = db_connection.cursor()

# lesson

subject_teacher = {'5ad9f270-d8f9-457b-9f68-e9b1c061c873': '58a6eaa0-09de-4908-839b-f021431fe275',
                   'd6c036a3-218b-412d-8330-9660387fb3c1': '068e9235-267a-4883-85dc-216f16bcfbda',
                   '0c9ffcaf-41ed-45f9-8e38-0b19bf9fb5fc': '078b847e-420e-4475-9215-5eca11db7741',
                   '14649c3a-6da2-4726-acf9-e3ae2a729c87': '20425018-1253-4b55-9c91-a4282c34e8e8',
                   '6dcbc8c3-d6be-4b9a-a506-7400ef459a06': '89bacf93-d772-4456-9198-949c58765c2d',
                   '930a4899-e971-4292-a147-e35da32a21ab': '58da4586-a48d-435b-a7f8-e5ea9a135a3e',
                   '708af9d0-93a0-438d-ad04-2467dfd1467a': '968109c5-c3e2-4e1a-bf63-383edde48609',
                   '5fb404c7-3838-4f48-87de-c92f264fe756': '00906757-0419-4ed5-9ca7-62181eaaf22e',
                   'b12c0d61-5641-4051-913a-e4d1fd703a56': '205b7819-26ae-4736-8ab7-f89898f4c3ae',
                   '777f69e2-69c6-4a15-a791-64138bf837b1': '58da4586-a48d-435b-a7f8-e5ea9a135a3e',
                   '1afa8aa6-305e-481e-9efc-eb1044a7eaa0': '205b7819-26ae-4736-8ab7-f89898f4c3ae',
                   '36faf1bc-d487-4fa7-9078-5738d22b901d': '968109c5-c3e2-4e1a-bf63-383edde48609',
                   'adc17f0c-006f-46a5-8aea-1bf0ec0af355': 'a403978a-43a6-421a-9717-7e1f65cf6907',
                   '7f5eaec2-d1ec-448f-8048-dc673d43c8ae': '89bacf93-d772-4456-9198-949c58765c2d',
                   '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85': '58a6eaa0-09de-4908-839b-f021431fe275',
                   'dab4c674-5075-4f56-b07b-bf0faa714c20': '44954d09-6323-4e4d-9318-4394ba4a43de',
                   '672c6450-3545-4bd2-b0f5-409e99e06f9b': '968109c5-c3e2-4e1a-bf63-383edde48609',
                   'ac77f49c-5003-43e6-9b6c-f8557db43755': '068e9235-267a-4883-85dc-216f16bcfbda',
                   '2d323c76-7d80-4406-9cc4-3ebdf50eff9c': '16f86aee-e622-40bb-8e35-e7c77c427390',
                   '7f5eaec2-d1ec-448f-8048-dc673d43c8ae': '9cc6ab26-4b69-444e-8e13-07315e17a62f',
                   'adc17f0c-006f-46a5-8aea-1bf0ec0af355': 'ba048b13-1dc1-4e8b-b972-66c0cfbfaba1'
}

for lesson in range(20):
        month = f'0{randint(1, 5)}'
        dayy_rand = randint(1, 31)
        dayy = f'0{dayy_rand}' if dayy_rand < 10 else dayy_rand
        day = f'2023-{month}-{dayy}'
        time = randint(8, 18)
        hour = f'0{time}' if time < 10 else time
        minutes = choice(['00', 15, 30, 45])
        precise_time = f'{hour}:{minutes}:00'
        subject_id = choice(list(subject_teacher.keys()))
        teacher_id = subject_teacher[subject_id]
        db_cursor.execute('INSERT INTO lesson (day, precise_time, subject_id, teacher_id) VALUES (%s, %s, %s, %s)', (day, precise_time, subject_id, teacher_id))
db_connection.commit()
db_cursor.execute('SELECT id from class')
class_ids = [i[0] for i in db_cursor.fetchall()]


db_cursor.close()
db_connection.close()