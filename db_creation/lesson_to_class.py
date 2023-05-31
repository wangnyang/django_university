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



"""
                  id                  |              subject_id              |               class_id               
--------------------------------------+--------------------------------------+--------------------------------------
 dc4d9d15-cda3-43d5-9585-26893428c8e8 | 5ad9f270-d8f9-457b-9f68-e9b1c061c873 | fb007626-be1b-4776-8a28-57c73bcacec3
 1c9e4673-2267-4a06-bf04-a65395ecfd39 | d6c036a3-218b-412d-8330-9660387fb3c1 | fb007626-be1b-4776-8a28-57c73bcacec3
 214db3b4-ea77-41fb-a162-5efdc5fe25e4 | 0c9ffcaf-41ed-45f9-8e38-0b19bf9fb5fc | fb007626-be1b-4776-8a28-57c73bcacec3
 b9891c61-c73e-4637-99e0-f0c4a4dab098 | 14649c3a-6da2-4726-acf9-e3ae2a729c87 | fb007626-be1b-4776-8a28-57c73bcacec3
 54463251-d7df-41a9-ab1b-4f8f310e48c7 | dab4c674-5075-4f56-b07b-bf0faa714c20 | fb007626-be1b-4776-8a28-57c73bcacec3
 c69c0b9e-2116-4147-8ea5-46d12b94cc9e | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | fb007626-be1b-4776-8a28-57c73bcacec3
 72c7dd00-58ab-442e-bd2e-1b6310030947 | 672c6450-3545-4bd2-b0f5-409e99e06f9b | fb007626-be1b-4776-8a28-57c73bcacec3
 5d370491-d9e7-455f-8fbb-013000dc1465 | ac77f49c-5003-43e6-9b6c-f8557db43755 | fb007626-be1b-4776-8a28-57c73bcacec3
 71db45ee-016f-4217-9c2f-165049314544 | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | fb007626-be1b-4776-8a28-57c73bcacec3
 26d5543a-4d7b-44cc-ae9b-1fc7f7d7cc22 | dab4c674-5075-4f56-b07b-bf0faa714c20 | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 cf7e8760-91ad-4bc8-8d23-bdc338152a44 | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 1ccb17a0-bae7-4cc5-af9b-59a0d6c29a6a | 672c6450-3545-4bd2-b0f5-409e99e06f9b | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 763043c2-ec8f-437c-b384-cdefb2750dfa | ac77f49c-5003-43e6-9b6c-f8557db43755 | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 33e8c47d-9b86-48dc-80c4-dc2e74bba0f2 | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 b6cfc726-66f0-452b-99ba-5ae05d45bb62 | 10f6450c-a111-45a2-ab76-4f684314b501 | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 070f2648-f478-480f-aab2-c5d2188ece2a | 36faf1bc-d487-4fa7-9078-5738d22b901d | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 ff421ff5-1593-4901-bebf-26ade84e93f3 | adc17f0c-006f-46a5-8aea-1bf0ec0af355 | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 039665af-b5e7-400e-af24-96983811c1bf | 7f5eaec2-d1ec-448f-8048-dc673d43c8ae | 7a6a2d88-b810-4ad2-bf46-6415a1a1c09a
 7b0074f0-93ea-4c18-bce3-aa3b794eab0a | dab4c674-5075-4f56-b07b-bf0faa714c20 | 1f86ff42-1c7c-4539-b230-587cede53598
 f9a3dd67-2000-4d49-b658-45a2ee173572 | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | 1f86ff42-1c7c-4539-b230-587cede53598
 8e2e9e4a-c8ab-4fca-bc6a-1790bbf8af30 | 672c6450-3545-4bd2-b0f5-409e99e06f9b | 1f86ff42-1c7c-4539-b230-587cede53598
 95059e14-e107-4a2d-b43a-b3a999c6fea8 | ac77f49c-5003-43e6-9b6c-f8557db43755 | 1f86ff42-1c7c-4539-b230-587cede53598
 183b1a99-a097-4332-a7a6-1a0d1d2d839d | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | 1f86ff42-1c7c-4539-b230-587cede53598
 02cb9d84-9d74-4c1a-a113-5a2c76b8e033 | 10f6450c-a111-45a2-ab76-4f684314b501 | 1f86ff42-1c7c-4539-b230-587cede53598
 6db56cb4-913d-4e10-a04d-34770dbf7bb5 | 36faf1bc-d487-4fa7-9078-5738d22b901d | 1f86ff42-1c7c-4539-b230-587cede53598
 e0dbf8a0-fe2c-4af8-ad4b-23f205878e5a | adc17f0c-006f-46a5-8aea-1bf0ec0af355 | 1f86ff42-1c7c-4539-b230-587cede53598
 64383537-eefc-41ad-a6b1-1d04a22aa350 | 7f5eaec2-d1ec-448f-8048-dc673d43c8ae | 1f86ff42-1c7c-4539-b230-587cede53598
 df4e0aec-fc7b-402e-b77a-86df4ddad0ce | dab4c674-5075-4f56-b07b-bf0faa714c20 | 155807b8-df6b-4bed-88b9-b20b785bca89
 f72a4965-0cfa-4c0c-a051-cacb624c988b | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | 155807b8-df6b-4bed-88b9-b20b785bca89
 329d134c-8f51-49c3-aeeb-ac4338e652e9 | 672c6450-3545-4bd2-b0f5-409e99e06f9b | 155807b8-df6b-4bed-88b9-b20b785bca89
 c62b76a5-3a38-471c-816b-e8174fc9f768 | ac77f49c-5003-43e6-9b6c-f8557db43755 | 155807b8-df6b-4bed-88b9-b20b785bca89
 469e419d-93de-423e-931b-d786a7f38cfa | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | 155807b8-df6b-4bed-88b9-b20b785bca89
 4cc6dbe0-7ed4-48ff-8908-ca501ba3bfed | 10f6450c-a111-45a2-ab76-4f684314b501 | 155807b8-df6b-4bed-88b9-b20b785bca89
 ebf1f769-9082-405b-9dd5-e27723f11200 | 36faf1bc-d487-4fa7-9078-5738d22b901d | 155807b8-df6b-4bed-88b9-b20b785bca89
 5b3a31ef-d471-41be-913c-99345f87fd2f | adc17f0c-006f-46a5-8aea-1bf0ec0af355 | 155807b8-df6b-4bed-88b9-b20b785bca89
 ee2f3d4b-1222-4690-8e4a-8188cdc5092d | 7f5eaec2-d1ec-448f-8048-dc673d43c8ae | 155807b8-df6b-4bed-88b9-b20b785bca89
 902d816a-6911-45a4-b5fa-ee34d1d37535 | dab4c674-5075-4f56-b07b-bf0faa714c20 | fd2b478e-a099-41c0-87e5-f7b3231f8906
 03e0baf3-3f82-4b51-a751-071fb14674d1 | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | fd2b478e-a099-41c0-87e5-f7b3231f8906
 277cd8ac-93b8-4a64-a302-d9a323550472 | 672c6450-3545-4bd2-b0f5-409e99e06f9b | fd2b478e-a099-41c0-87e5-f7b3231f8906
 575f60be-6c92-438e-a3a7-6c9b92a0afb1 | ac77f49c-5003-43e6-9b6c-f8557db43755 | fd2b478e-a099-41c0-87e5-f7b3231f8906
 a1e5538f-c918-4fed-b0ea-28afdd3a44da | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | fd2b478e-a099-41c0-87e5-f7b3231f8906
 ffcf006b-ec47-42e2-bd13-737afd780ee5 | 36faf1bc-d487-4fa7-9078-5738d22b901d | fd2b478e-a099-41c0-87e5-f7b3231f8906
 99003320-72ad-444f-9ac6-e9d239d1a7f6 | adc17f0c-006f-46a5-8aea-1bf0ec0af355 | fd2b478e-a099-41c0-87e5-f7b3231f8906
 17086986-2f06-486c-955d-df66e6b6952c | 7f5eaec2-d1ec-448f-8048-dc673d43c8ae | fd2b478e-a099-41c0-87e5-f7b3231f8906
 0b6d9b5d-06ed-473c-ae51-5f022455a305 | dab4c674-5075-4f56-b07b-bf0faa714c20 | 6a1b08db-9da3-4273-8874-aa65e2f43fdb
 2de4e0d8-e97a-48b6-92a2-5c8065f53c28 | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | 6a1b08db-9da3-4273-8874-aa65e2f43fdb
 f873f77d-9c94-4534-bee4-0ade40e42e07 | 672c6450-3545-4bd2-b0f5-409e99e06f9b | 6a1b08db-9da3-4273-8874-aa65e2f43fdb
 bb506db9-d757-4f82-bfbe-42c6d3c46279 | ac77f49c-5003-43e6-9b6c-f8557db43755 | 6a1b08db-9da3-4273-8874-aa65e2f43fdb
 ddfeab67-c46c-40c0-a820-b8f03caac695 | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | 6a1b08db-9da3-4273-8874-aa65e2f43fdb
 4b412ff8-31cc-4873-8af7-1e2739dcc4c4 | 6dcbc8c3-d6be-4b9a-a506-7400ef459a06 | 6a1b08db-9da3-4273-8874-aa65e2f43fdb
 a0526cf9-0b73-4564-a09c-45b814efefd2 | 930a4899-e971-4292-a147-e35da32a21ab | 6a1b08db-9da3-4273-8874-aa65e2f43fdb
 7027db62-b1f6-494d-9a12-9a2680ef80f8 | 5fb404c7-3838-4f48-87de-c92f264fe756 | 6a1b08db-9da3-4273-8874-aa65e2f43fdb
 a0010825-18d0-4078-ae8e-8a723b114183 | dab4c674-5075-4f56-b07b-bf0faa714c20 | 4120f860-e198-4ed4-a94d-3095ed0b63f3
 47cae198-574f-4bb9-8dfd-65f99dc07408 | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | 4120f860-e198-4ed4-a94d-3095ed0b63f3
 770d8a72-133a-4b58-ad1e-4f1f32672961 | 672c6450-3545-4bd2-b0f5-409e99e06f9b | 4120f860-e198-4ed4-a94d-3095ed0b63f3
 ee62ce01-ce8d-475a-a50a-6d62493730ca | ac77f49c-5003-43e6-9b6c-f8557db43755 | 4120f860-e198-4ed4-a94d-3095ed0b63f3
 b80bc83e-0bc0-455e-8662-80acbfc4e31b | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | 4120f860-e198-4ed4-a94d-3095ed0b63f3
 8ab45d74-0a6f-401d-93f5-2a7c69f54e74 | 6dcbc8c3-d6be-4b9a-a506-7400ef459a06 | 4120f860-e198-4ed4-a94d-3095ed0b63f3
 6dd665d5-2c3f-4270-80af-2775e3ba3674 | 930a4899-e971-4292-a147-e35da32a21ab | 4120f860-e198-4ed4-a94d-3095ed0b63f3
 ed064e05-4cb6-49cb-9126-91a9bfa6047f | 5fb404c7-3838-4f48-87de-c92f264fe756 | 4120f860-e198-4ed4-a94d-3095ed0b63f3
 308f2afa-668d-4240-ad20-629c7b348975 | dab4c674-5075-4f56-b07b-bf0faa714c20 | 90c896e8-b02d-4490-a4a9-88f94422a03e
 f0471e30-c449-46da-b356-94b1192af491 | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | 90c896e8-b02d-4490-a4a9-88f94422a03e
 5a3f3e80-7573-4a5f-ba60-92c8260f8a7c | 672c6450-3545-4bd2-b0f5-409e99e06f9b | 90c896e8-b02d-4490-a4a9-88f94422a03e
 eb46b9a9-295c-4c0b-9a22-4e41b46d20ca | ac77f49c-5003-43e6-9b6c-f8557db43755 | 90c896e8-b02d-4490-a4a9-88f94422a03e
 ad518700-5c4b-4431-920b-8069674dd5d7 | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | 90c896e8-b02d-4490-a4a9-88f94422a03e
 7d13612e-3bba-42b9-976d-9619f284d8c1 | 6dcbc8c3-d6be-4b9a-a506-7400ef459a06 | 90c896e8-b02d-4490-a4a9-88f94422a03e
 cee95ec1-cc75-4730-a816-7fa35ee6a12d | 930a4899-e971-4292-a147-e35da32a21ab | 90c896e8-b02d-4490-a4a9-88f94422a03e
 9e4dbc40-3082-4b5d-a8e6-a2b7367ac171 | 5fb404c7-3838-4f48-87de-c92f264fe756 | 90c896e8-b02d-4490-a4a9-88f94422a03e
 a6428eaf-b8d4-48b2-a4bc-e1c49a87b970 | dab4c674-5075-4f56-b07b-bf0faa714c20 | 518cfc79-aeca-4b4b-86c3-b8592bbc33e8
 0c1dcb6c-88ed-43b2-b057-1c0ac57863be | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | 518cfc79-aeca-4b4b-86c3-b8592bbc33e8
 43ab86c4-d721-4fc5-af7a-f842ca30cfc7 | 672c6450-3545-4bd2-b0f5-409e99e06f9b | 518cfc79-aeca-4b4b-86c3-b8592bbc33e8
 2f73ec8e-e02a-4c18-a0d8-ca7a64920f0c | ac77f49c-5003-43e6-9b6c-f8557db43755 | 518cfc79-aeca-4b4b-86c3-b8592bbc33e8
 7c9e2127-c6f6-40fc-945f-599d08b33526 | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | 518cfc79-aeca-4b4b-86c3-b8592bbc33e8
 eb3450c8-e47f-4e73-ae48-8fc1fdec4fbf | 6dcbc8c3-d6be-4b9a-a506-7400ef459a06 | 518cfc79-aeca-4b4b-86c3-b8592bbc33e8
 ea09b18b-3517-46c8-92ad-efa0b586bcdf | 930a4899-e971-4292-a147-e35da32a21ab | 518cfc79-aeca-4b4b-86c3-b8592bbc33e8
 1a258a10-6700-4bd0-87b3-1a83423a1dc3 | 5fb404c7-3838-4f48-87de-c92f264fe756 | 518cfc79-aeca-4b4b-86c3-b8592bbc33e8
 22500229-d80c-4e19-bc8a-210df5541f36 | dab4c674-5075-4f56-b07b-bf0faa714c20 | 5d57048b-8230-4308-b3ae-334db3a792de
 6732bf26-d93a-4c98-8a10-1383fef6ba39 | 18811ed7-a6dd-4a2e-b1e9-4b0da348dc85 | 5d57048b-8230-4308-b3ae-334db3a792de
 48d51a7e-231a-4f6c-888e-bd9fd757f39e | 672c6450-3545-4bd2-b0f5-409e99e06f9b | 5d57048b-8230-4308-b3ae-334db3a792de
 0778c6eb-caff-49ab-a46b-0bc8103795ca | ac77f49c-5003-43e6-9b6c-f8557db43755 | 5d57048b-8230-4308-b3ae-334db3a792de
 c112d37d-ed8b-44b0-b542-3eb2696503a3 | 2d323c76-7d80-4406-9cc4-3ebdf50eff9c | 5d57048b-8230-4308-b3ae-334db3a792de
 e16d2331-e799-4456-a487-5eb16c06490a | b12c0d61-5641-4051-913a-e4d1fd703a56 | 5d57048b-8230-4308-b3ae-334db3a792de
 b16c7c51-8024-4ec3-9464-66a3a9f0c1f0 | 777f69e2-69c6-4a15-a791-64138bf837b1 | 5d57048b-8230-4308-b3ae-334db3a792de
 72ee91f9-1714-4c46-ac4b-d6e58ad3ecd0 | 1afa8aa6-305e-481e-9efc-eb1044a7eaa0 | 5d57048b-8230-4308-b3ae-334db3a792de
 
"""


lesson_to_class = {'2d323c76-7d80-4406-9cc4-3ebdf50eff9c': 'fb007626-be1b-4776-8a28-57c73bcacec3',
                   '6dcbc8c3-d6be-4b9a-a506-7400ef459a06': '6a1b08db-9da3-4273-8874-aa65e2f43fdb',
                   '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85': 'fb007626-be1b-4776-8a28-57c73bcacec3',
                   'd6c036a3-218b-412d-8330-9660387fb3c1': 'fb007626-be1b-4776-8a28-57c73bcacec3',
                   '1afa8aa6-305e-481e-9efc-eb1044a7eaa0': '5d57048b-8230-4308-b3ae-334db3a792de',
                   '5ad9f270-d8f9-457b-9f68-e9b1c061c873': 'fb007626-be1b-4776-8a28-57c73bcacec3',
                   'ac77f49c-5003-43e6-9b6c-f8557db43755': 'fd2b478e-a099-41c0-87e5-f7b3231f8906',
                   '5fb404c7-3838-4f48-87de-c92f264fe756': '90c896e8-b02d-4490-a4a9-88f94422a03e',
                   '672c6450-3545-4bd2-b0f5-409e99e06f9b': '90c896e8-b02d-4490-a4a9-88f94422a03e',
                   'dab4c674-5075-4f56-b07b-bf0faa714c20': '518cfc79-aeca-4b4b-86c3-b8592bbc33e8',
                   'adc17f0c-006f-46a5-8aea-1bf0ec0af355': 'fd2b478e-a099-41c0-87e5-f7b3231f8906',
                   '36faf1bc-d487-4fa7-9078-5738d22b901d': '155807b8-df6b-4bed-88b9-b20b785bca89',
}

lesson_id = ''
used_lessons = []
for subject_id, class_id in lesson_to_class.items():
    db_cursor.execute(f"select id from lesson where subject_id='{subject_id}'")
    lesson_ids = db_cursor.fetchall()
    print(lesson_ids, '***')
    for i in lesson_ids:
        if i[0] not in used_lessons:
            lesson_id = i[0]
            used_lessons.append(i[0])
    db_cursor.execute('insert into lesson_to_class (lesson_id, class_id) values (%s, %s)', (lesson_id, class_id))

lesson_to_class_2 = {'6dcbc8c3-d6be-4b9a-a506-7400ef459a06': '518cfc79-aeca-4b4b-86c3-b8592bbc33e8',
                     'd6c036a3-218b-412d-8330-9660387fb3c1': 'fb007626-be1b-4776-8a28-57c73bcacec3',
                     '1afa8aa6-305e-481e-9efc-eb1044a7eaa0': '5d57048b-8230-4308-b3ae-334db3a792de',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755': '5d57048b-8230-4308-b3ae-334db3a792de',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b': '5d57048b-8230-4308-b3ae-334db3a792de',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85': '5d57048b-8230-4308-b3ae-334db3a792de',
                     'adc17f0c-006f-46a5-8aea-1bf0ec0af355': 'fd2b478e-a099-41c0-87e5-f7b3231f8906',
}

lesson_to_class_3 = {
                     'd6c036a3-218b-412d-8330-9660387fb3c1': 'fb007626-be1b-4776-8a28-57c73bcacec3',
                     '1afa8aa6-305e-481e-9efc-eb1044a7eaa0': '5d57048b-8230-4308-b3ae-334db3a792de',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755': '6a1b08db-9da3-4273-8874-aa65e2f43fdb',
}
    
for subject_id, class_id in lesson_to_class_2.items():
    print(class_id, subject_id)
    db_cursor.execute(f"select id from lesson where subject_id='{subject_id}'")
    lesson_ids = db_cursor.fetchall()
    for i in lesson_ids:
        if i not in used_lessons:
            lesson_id = i
            used_lessons.append(i)
    db_cursor.execute('insert into lesson_to_class (lesson_id, class_id) values (%s, %s)', (lesson_id, class_id))

for subject_id, class_id in lesson_to_class_3.items():
    print(class_id, subject_id)
    db_cursor.execute(f"select id from lesson where subject_id='{subject_id}'")
    lesson_ids = db_cursor.fetchall()
    for i in lesson_ids:
        if i not in used_lessons:
            lesson_id = i
            used_lessons.append(i)
    db_cursor.execute('insert into lesson_to_class (lesson_id, class_id) values (%s, %s)', (lesson_id, class_id))
db_connection.commit()
db_cursor.close()
db_connection.close()
