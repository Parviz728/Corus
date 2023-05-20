import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="corus",
    user="corus_user",
    password="test1234"
)
cur = conn.cursor()
# создание таблицы book
'''
cur.execute("""CREATE TABLE book(
    book_id serial PRIMARY KEY,
    name text,
    author text,
    press text,
    press_city text,
    pages int,
    example_id int,
    date_of_comming date,
    FOREIGN KEY (example_id) REFERENCES books_issue(example_id)
)
""")
conn.commit()
'''

with open("Задача3_Книги.csv", 'r', encoding='cp1251') as file:
    reader = csv.reader(file)
    next(reader) # Skip the header row
    cur.execute("SELECT books_issue.example_id from books_issue")
    example_ids = set()
    used = set()
    for i in list(cur):
        example_ids.add(i[0])
    for row in reader:
        if len(row) == 1:
            row = row[0].split(';')
        else:
            row = (row[0] + row[1]).split(';')
        if len(row) == 8:
            if not row[5].isdigit():
                res = ''
                for digit in row[5]:
                    if digit.isdigit():
                        res += digit
                row[5] = res
            if not row[6].isdigit():
                res = ''
                for digit in row[6]:
                    if digit.isdigit():
                        res += digit
                row[6] = res
            guess = int(row[6])
            if guess in example_ids:
                cur.execute(
                    "INSERT INTO book VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    row
                )
conn.commit()
