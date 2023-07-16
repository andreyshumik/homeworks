import sqlite3
import random


class ExampleDB:
    def __init__(self):
        self.conn = sqlite3.connect('name.db')
        self.cursor = self.conn.cursor()

    def view (self):
        self.cursor.execute('''SELECT * FROM tab_1''')
        k = self.cursor.fetchall()
        print(k)

    def one_arg(self):
        self.cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (3)''')
        self.conn.commit()

        self.view()

    def two_arg(self):
        self.cursor.execute('''SELECT id FROM tab_1''')
        k = self.cursor.fetchall()
        self.cursor.execute('''DELETE FROM tab_1 WHERE id = ?''', (k[0]))
        self.conn.commit()

        self.view()

    def three_arg(self):
        self.cursor.execute('''SELECT id FROM tab_1''')
        k = self.cursor.fetchall()
        self.cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = ?''', (k[2]))
        self.conn.commit()

        self.view()


    def create(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

        for i in range(7):
            x = int(random.randint(1,9))
            self.cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (x,))
        self.conn.commit()

        self.view()

    def argumenty(self, *args):
        if len(args) == 1:
            self.one_arg()
        if len(args) == 2 and type(args[1]) == int:
            self.two_arg()
        if len(args) == 3 and type(args[2]) == int:
            self.three_arg()





a = ExampleDB()
#a.create()   #создание рандомной базы данных
a.view()
a.argumenty(1)
a.argumenty(1,2)
a.argumenty(1,2,3)