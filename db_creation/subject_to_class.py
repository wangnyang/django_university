import psycopg2
from dotenv import load_dotenv
from os import getenv

load_dotenv()
PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')


db_connection = psycopg2.connect(dbname=PG_DBNAME, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)
db_cursor = db_connection.cursor()


subjects = [['5ad9f270-d8f9-457b-9f68-e9b1c061c873', 
                     'd6c036a3-218b-412d-8330-9660387fb3c1',
                     '0c9ffcaf-41ed-45f9-8e38-0b19bf9fb5fc',
                     '14649c3a-6da2-4726-acf9-e3ae2a729c87',
                     'dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c'
                     ],
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',
                     '10f6450c-a111-45a2-ab76-4f684314b501',
                     '36faf1bc-d487-4fa7-9078-5738d22b901d',
                     'adc17f0c-006f-46a5-8aea-1bf0ec0af355',
                     '7f5eaec2-d1ec-448f-8048-dc673d43c8ae'
                     ],
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',
                     '10f6450c-a111-45a2-ab76-4f684314b501',
                     '36faf1bc-d487-4fa7-9078-5738d22b901d',
                     'adc17f0c-006f-46a5-8aea-1bf0ec0af355',
                     '7f5eaec2-d1ec-448f-8048-dc673d43c8ae'
                     ],
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',
                     '10f6450c-a111-45a2-ab76-4f684314b501',
                     '36faf1bc-d487-4fa7-9078-5738d22b901d',
                     'adc17f0c-006f-46a5-8aea-1bf0ec0af355',
                     '7f5eaec2-d1ec-448f-8048-dc673d43c8ae'
                     ],
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',  #
                     '36faf1bc-d487-4fa7-9078-5738d22b901d',
                     'adc17f0c-006f-46a5-8aea-1bf0ec0af355',
                     '7f5eaec2-d1ec-448f-8048-dc673d43c8ae'
                     ],
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',  #
                     '6dcbc8c3-d6be-4b9a-a506-7400ef459a06',
                     '930a4899-e971-4292-a147-e35da32a21ab',
                     '5fb404c7-3838-4f48-87de-c92f264fe756'
                     ],    # Economics
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',  #
                     '6dcbc8c3-d6be-4b9a-a506-7400ef459a06',
                     '930a4899-e971-4292-a147-e35da32a21ab',
                     '5fb404c7-3838-4f48-87de-c92f264fe756'
                     ],    # Economics 2
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',  #
                     '6dcbc8c3-d6be-4b9a-a506-7400ef459a06',
                     '930a4899-e971-4292-a147-e35da32a21ab',
                     '5fb404c7-3838-4f48-87de-c92f264fe756'
                     ],    # Economics 3
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',  #
                     '6dcbc8c3-d6be-4b9a-a506-7400ef459a06',
                     '930a4899-e971-4292-a147-e35da32a21ab',
                     '5fb404c7-3838-4f48-87de-c92f264fe756'
                     ],    # Mathematics 1
                     ['dab4c674-5075-4f56-b07b-bf0faa714c20',
                     '18811ed7-a6dd-4a2e-b1e9-4b0da348dc85',
                     '672c6450-3545-4bd2-b0f5-409e99e06f9b',
                     'ac77f49c-5003-43e6-9b6c-f8557db43755',
                     '2d323c76-7d80-4406-9cc4-3ebdf50eff9c',  #
                     'b12c0d61-5641-4051-913a-e4d1fd703a56',
                     '777f69e2-69c6-4a15-a791-64138bf837b1',
                     '1afa8aa6-305e-481e-9efc-eb1044a7eaa0'
                     ]
                     ]

classes = ['fb007626-be1b-4776-8a28-57c73bcacec3',    # linguistics
                     '7a6a2d88-b810-4ad2-bf46-6415a1a1c09a',    # archaeology 1
                     '1f86ff42-1c7c-4539-b230-587cede53598',    # archaeology 2
                     '155807b8-df6b-4bed-88b9-b20b785bca89',     # archaeology 3
                     'fd2b478e-a099-41c0-87e5-f7b3231f8906',    # anthropology
                     '6a1b08db-9da3-4273-8874-aa65e2f43fdb',    # Economics
                     '4120f860-e198-4ed4-a94d-3095ed0b63f3',    # Economics 2
                     '90c896e8-b02d-4490-a4a9-88f94422a03e',    # Economics 3
                     '518cfc79-aeca-4b4b-86c3-b8592bbc33e8',    # Mathematics 1
                     '5d57048b-8230-4308-b3ae-334db3a792de']    # Mathematics 2

for i in range(len(classes)):
    for subject_id in subjects[i]:
        db_cursor.execute('INSERT INTO subject_to_class (subject_id, class_id) values (%s, %s)', (subject_id, classes[i]))

db_connection.commit()