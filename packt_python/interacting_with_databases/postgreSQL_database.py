#first, you need to install postgreSQL from their website
#make sure it is for the correct platform you are using (Windows, Linux, etc)
#be sure to remember your password and other things from the installation
#once everything is downloaded, use pip install to install psycopg2
#you may bump into an error with the Windows version
#there are different ways to solve this problem:
    #download Visual Studio Code
    #use precompiled libraries, and you can find those on the webpage by Christoph Gohlk
        #look for psycopg2 wheel (whl) file for the right system (Windows, Linux, etc)
        #wheel files can be downloaded with pip
        #once you find the right one, download it and move it to the desired python folder (in my case, packt_python\interacting_with_databases)
        #pip install the wheel file you just moved into the folder
        #you can check if the wheel file installed properly in the python interactive shell
        #to find out what version it is, type psycopg2.__version__ in the python interactive shell

import psycopg2

def create_table():
    connection = psycopg2.connect("dbname='database1' user='postgres' password='cooper10' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='cooper10' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect("dbname='database1' user='postgres' password='cooper10' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='cooper10' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='cooper10' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    connection.commit()
    connection.close()

create_table()
update(20,15.0,'Apple')
#insert("Apple",10,15)
print(view())
#delete("Orange")

