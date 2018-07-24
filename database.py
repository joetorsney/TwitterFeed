import sqlite3 as s

class Database():

    def __init__(self, db):
        self.conn = s.connect(db)
        self.c = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS Tweets(unix INTEGER, text TEXT)")
        self.conn.commit()

    def addTweet(self, unix, text):
        self.c.execute("INSERT INTO Tweets(unix, text) VALUES(?,?)", (unix, text))
        self.conn.commit()
