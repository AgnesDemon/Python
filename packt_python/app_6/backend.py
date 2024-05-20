import sqlite3

class Database:

    def __init__(self,db): #adding self gives this function a paramter, which will allow for one parameter to be called
        #connection = sqlite3.connect("books.db") #creates connection with window
        #OPTIONAL! You can add another parameter, "db", and replace "books.db" with "db"
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.connection.commit()
        #connection.close()

    def insert(self,title, author, year, isbn):
        #connection = sqlite3.connect("books.db")
        #cursor = connection.cursor()
        self.cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
        self.connection.commit()
        #self.connection.close()

    def view(self):
        #connection = sqlite3.connect("books.db")
        #cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM  book")
        rows = self.cursor.fetchall()
        #self.connection.close()
        return rows

    def search(self,title="",author="",year="",isbn=""): #passing empty strings as default, which prevents an error
        #connection = sqlite3.connect("books.db")
        #cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = self.cursor.fetchall()
        #self.connection.close()
        return rows

    def delete(self,id):
        #connection = sqlite3.connect("books.db")
        #cursor = connection.cursor()
        self.cursor.execute("DELETE FROM book WHERE id=?", (id,))
        self.connection.commit()
        #self.connection.close()

    def update(self,id,title,author,year,isbn):
        #connection = sqlite3.connect("books.db")
        #cursor = connection.cursor()
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.connection.commit()
        #self.connection.close()
    
    def __del__(self):
        self.connection.close()


    #connect()
#update(3,"Little Women","Louisa May Alcott",1868,123456789)
#delete(1)
#insert("Oliver Twist","Charles Dickens",1837,124124124)
#print(view())
#print(search(year=1868))
