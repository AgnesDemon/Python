import sqlite3

class Database:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS personal_manga_library (id INTEGER PRIMARY KEY, name text, volume integer, author text)")
        self.connection.commit()
    
    def insert(self,name,volume,author):
        self.cursor.execute("INSERT INTO personal_manga_library VALUES (NULL,?,?,?)", (name,volume,author))
        self.connection.commit()
    
    def view_all_manga(self):
        self.cursor.execute("SELECT * FROM personal_manga_library")
        rows = self.cursor.fetchall()
        return rows
    
    def search_volume(self,name="",volume="",author=""):
        self.cursor.execute("SELECT * FROM personal_manga_library WHERE name=? OR volume=? or author=?", (name,volume,author))
        rows = self.cursor.fetchall()
        return rows
    
    def delete(self,id):
        self.cursor.execute("DELETE FROM personal_manga_library WHERE id=?", (id,))
        self.connection.commit()

    def update(self,id,name,volume,author):
        self.cursor.execute("UPDATE personal_manga_library SET name=?, volume=?, author=? WHERE id=?", (name,volume,author,id))
        self.connection.commit()
    
    def __del__(self):
        self.connection.close()



