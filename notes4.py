
#Functions
def printMe (str):
    print (str)
    return

def greetUser (username):
    print("welcome, " + username)

greetUser("Isabel")

#Let's say that the user name is now known because they logged in or something
users = {"Isa" : "Isabel", "Monch": "Leonardo", "Mommy" : "Livier", "Daddy" : "Leonard"}
tempname = ""
def greetUser (username):
    fullname = users[username]
    print(fullname)
    global tempname
   
    return fullname

#The squigly line that appears under "fullname" means it won't work because it is not part of the code above
#print(fullname)

name = greetUser("Isa")
print("Welcome, " + name)

people = {"Leo" : 41, "Munch" : 15, "Isabel" : 17, "Livier" : 36}
numbers = {27 : "R", 35 : "Z", 96 : "N", 1 : "A", 13 : "C"}

print(max(people))
print(max(numbers))


# do function with optimal parameter/argument
def optional (firstName, lastName = ""):
    print("Hello " + firstName + " "+ lastName)
    return

optional("John", "Doe")
optional("Jane")

# " " or "word " both allow spaces, otherwise words end up together

# take in data
print("Enter the Password")
password = input()
print("Password: " + password)


users = {"Isa" : "Isabel", "Monch": "Leonardo", "Mommy" : "Livier", "Daddy" : "Leonard"}

def getUser (username):
    fullname = users[username]
    return fullname

def login ():
    print("Enter your username:")
    username = input()
    return username

user = login()
print("Hello " + getUser(user))

#Assignment: using the login above, use a while lopp to make the system keep asking for a username until the user provides a username from your list
#if user gives right username, say something like "Login Successful"
#if user gives wrong username, say something like "Login Failed", ask for the username again
#Code needed for assignment:
def checkUser (username):
    if username is users:
        return True
    else:
        return False

def getUser (username):
    fullname = users[username]
    return fullname

def login ():
    print("Enter your username:")
    username = input()
    return username

user = login()
validUser = checkUser(user)
if validUser:
    print("Hello " + getUser(user))
