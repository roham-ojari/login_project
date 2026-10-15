
import sqlite3

class database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS
        Contact (id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,email TEXT,password TEXT)''')
        self.con.commit()

    def insert_record(self,fname,lname,email,password):
        self.cur.execute(
        "INSERT INTO Contact (fname,lname,email,password) VALUES (?, ?, ?, ?)",(fname,lname,email,password))
        self.con.commit()
    def search(self,email,password):

        self.cur.execute('''SELECT * FROM Contact WHERE email = ? and password = ?     ''',(email,password))
        recs = self.cur.fetchall()
        return recs