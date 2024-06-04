import os
clear = lambda: os.system('cls')

users = {"AgnesDemon13" : "Agnes"}

def getUser (username):
    name = users[username]
    return name

def login():
    print("Welcome to your local Manga Organizer! Please enter your username: ")
    username = input()
    clear()
    return username

def checkUser(username):
    if username in users:
        return True
    else:
        return False

loggedIn = False
while loggedIn == False:
    user = login()
    validUser = checkUser(user)
    if validUser:
        loggedIn = True
        print("Welcome, " + getUser(user))
    else:
        print("Invalid login. Please try again.")

