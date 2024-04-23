import sqlite3

def create_table():
    connection =sqlite3.connect("lite.db") #connects to database
    cursor = connection.cursor() #creates the cursor
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #will create a table if one does not already exist
    cursor.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
    connection.commit() #commits changes to the database
    connection.close() #closes the connection to the database

def insert(item, quantity, price):
    connection =sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()

insert("Coffee Cup", 10, 5)


def view():
    connection =sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows

print(view())
