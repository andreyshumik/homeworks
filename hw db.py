import sqlite3
import random

conn = sqlite3.connect('name.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

# for i in range(5):
#     x = int(random.randint(1,9))
#     cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (x,))

conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)


def one_arg():
    cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (3)''')
    conn.commit()
def two_arg():
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
    conn.commit()
def three_arg():
    cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = 3''')
    conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)