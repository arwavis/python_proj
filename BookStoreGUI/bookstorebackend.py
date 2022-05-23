# pylint: disable=redefined-builtin
import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()
        # conn.close()

    def insert(self, title, author, year, isbn):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("INSERT INTO book  VALUES (NULL,?,?,?,?)",
                         (title, author, year, isbn))
        self.conn.commit()
        # conn.close()

    def view(self):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        # conn.close()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute(
            "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        # conn.close()
        return rows

    def delete(self, id):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("DELETE FROM book WHERE id =?", (id,))
        self.conn.commit()
        # conn.close()

    def update(self, id, title, author, year, isbn):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("UPDATE book SET title =?, author =?, year =?, isbn=? WHERE id =?", (
            title, author, year, isbn, id))
        self.conn.commit()
        # conn.close()

    def __del__(self):
        self.conn.close()

        # print(Database.view())
        # insert("The Moon", "Ardit suluce", 1985, 23546798)
        # print(view())
        # # delete(2)
        # print(view())
        # print(search(author="John Tablet"))
        # update(1, "The Sea salt", "John Tablet", 1932, 91234532)
