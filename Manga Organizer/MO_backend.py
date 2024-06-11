import sqlite3

class Database:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name text, volume integer, author text)")
        self.connection.commit()



