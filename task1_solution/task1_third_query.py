import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="corus",
    user="corus_user",
    password="test1234"
)
cur = conn.cursor()
'''
cur.execute("""CREATE TABLE customers(
    library_card serial PRIMARY KEY,
    surname varchar(50),
    name varchar(50),
    patronymic varchar(50),
    birthdate date,
    sex varchar(30),
    address varchar(70),
    phone_number varchar(30)
)
""")
conn.commit()
'''

with open("Задача3_Читатели.csv", 'r', encoding='cp1251') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if len(row) == 1:
            row = row[0].split(';')
            if '' in row:
                row.remove('')
        else:
            row = (row[0] + row[1]).split(';')
            if '' in row:
                row.remove('')
        if len(row) == 8:
            cur.execute(
                "INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                row
            )
conn.commit()