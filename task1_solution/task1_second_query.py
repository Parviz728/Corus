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
cur.execute("""CREATE TABLE books_issue(
    example_id serial PRIMARY KEY,
    on_date date,
    off_date date,
    library_card int,
    FOREIGN KEY (library_card) REFERENCES customers(library_card)
)
""")
conn.commit()
'''

with open("Задача3_Выдачи книг.csv", 'r', encoding='cp1251') as file:
    reader = csv.reader(file)
    next(reader)
    cur.execute("SELECT customers.library_card from customers")
    lst = set()
    used = set()
    for i in list(cur):
        lst.add(i[0])
    for row in reader:
        row = row[0].split(';')
        guess = int(row[-1])
        if int(row[0]) not in used:
            used.add(int(row[0]))
            if guess in lst:
                cur.execute(
                        "INSERT INTO books_issue VALUES (%s, %s, %s, %s)",
                        row
                    )
conn.commit()