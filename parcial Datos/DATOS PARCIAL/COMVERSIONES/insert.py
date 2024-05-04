import sqlite3

conn = sqlite3.connect("examen.db")

cursor = conn.cursor()

_SQL = """
CREATE TABLE if not exists mines(
mine_name text primary key,
FOREIGN KEY (product_id) REFERENCES products(idProduct));
"""

cursor.execute(_SQL)

with open("mine.sql", "r", encoding="UTF-8") as f:
    for i in f.read().split("\n"):
        cursor.execute(i)
        conn.commit()


_SQL = """
select * from mine;
"""

cursor.execute(_SQL)

data = cursor.fetchall()

for i in data:
    print(i)