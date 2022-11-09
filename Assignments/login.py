#Assignment: using the login above, use a while loop to make the system keep asking for a username until the user provides a username from your list
#if user gives right username, say something like "Login Successful"
#if user gives wrong username, say something like "Login Failed", ask for the username again
#Code needed for assignment:
'''users = {"Isa" : "Isabel", "Monch": "Leonardo", "Mommy" : "Livier", "Daddy" : "Leonard"}

def getUser (username):
    fullname = users[username]
    return fullname

def checkUser (username):
    if username in users:
        return True
    else:
        return False

def login ():
    print("Enter your username:")
    username = input()
    return username

user = login()
validUser = checkUser(user)
if validUser:
    print("Hello " + getUser(user))

while x <= loops:
    x += 1
    print("X" * (loops))
'''

users = {"Chavez" : "Isabel Aguillon", "Popcorn" : "Leonardo Aguillon", "Donald" : "Donald Martin", "Anna" : "Annabel Aguillon"}

def getUser (username):
    fullname = users[username]
    return fullname

def login ():
    print("Enter Username Please:")
    username = input()
    return username

def checkUser (username):
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
        print("Hello " + getUser(user))
    else:
        print("Login Failed")



'''
# messed up the terminal
#while validUser:
    validUser = checkUser(user)
#else:
    print("Incorrect")

#error
#while getUser:
    fullname = users[username]
    username = True
#else:
    print("Incorrect")

#(while True:) will go infinitely
#(while username:) username does not work
'''

'''user = login()
validUser = checkUser(user)
if validUser:
    print("Hello " + getUser(user))'''