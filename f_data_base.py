import sqlite3
import math
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fletchall()
            if res:
                return res
        except:
            print('Error reading from db')
        return []

    def add_post(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?)', (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f'Ошибка добавления статьи {e}')
            return False
        return True

