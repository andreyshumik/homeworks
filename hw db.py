import sqlite3
import random

conn = sqlite3.connect('name.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
#
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
    cursor.execute('''SELECT id FROM tab_1''')
    k = cursor.fetchall()
    cursor.execute('''DELETE FROM tab_1 WHERE id = ?''', (k[0]))
    conn.commit()
def three_arg():
    cursor.execute('''SELECT id FROM tab_1''')
    k = cursor.fetchall()
    cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = ?''', (k[2]))
    conn.commit()


def argumenty(*args):
    if len(args) == 1:
        one_arg()
    if len(args) == 2 and type(args[1]) == int :
        two_arg()
    if len(args) == 3 and type(args[2]) == int:
        three_arg()



cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)


argumenty(1,2,2)