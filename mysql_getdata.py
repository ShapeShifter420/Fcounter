import datetime
import pymysql
from threading import *


class BD:
    def __init__(self, bd_name):
        self.con = pymysql.connect('localhost', 'root',
                                   'toor', bd_name)

    def get_day(self, id, date):
        with self.con:
            cur = self.con.cursor()
            s = "SELECT * FROM unique_visitors WHERE id={} and date=\"{}\""
            cur.execute(s.format(id, date))
            count = cur.rowcount
        return count

    def get_month(self, id, date):
        with self.con:
            cur = self.con.cursor()
            s = "SELECT * FROM unique_visitors " \
                "WHERE id={} and date LIKE \"{}\""
            cur.execute(s.format(id, "%" + date[3:]))
            count = cur.rowcount
        return count

    def get_year(self, id, date):
        with self.con:
            cur = self.con.cursor()
            s = "SELECT * FROM unique_visitors " \
                "WHERE id={} and date LIKE \"{}\""
            cur.execute(s.format(id, "%" + date[6:]))
            count = cur.rowcount
        return count

    def get_all(self, id):
        with self.con:
            cur = self.con.cursor()
            cur.execute("SELECT * FROM unique_visitors WHERE id=%s", id)
            count = cur.rowcount
        return count

    def get_next_id(self):
        lock = Lock()
        lock.acquire()
        try:
            with self.con:
                cur = self.con.cursor()
                cur.execute("SELECT * FROM next_id")
                next_id = cur.fetchone()[0]
                s = "UPDATE next_id SET id={} WHERE id={}"
                cur.execute(s.format(next_id + 1, next_id))
            return next_id
        finally:
            lock.release()

    def set_visit(self, id, date):
        with self.con:
            cur = self.con.cursor()
            s = "insert into unique_visitors (id,date) value ("
            cur.execute(s + str(id) + ",\"" + date + "\")")


def get_date():
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%Y")
