#Homework:
#Require proper login with only 3 attempts. If they fail, they will be forced to exit the app
#Receipt calculator - Ask for the amounts, take in x amount of receipts.
#When done, display the rounded total
#Print receipts taken in: line by line, sort list by least to most expensive $xx
#No decimal places because it is rounded
#Bonus items: keep the screen clean (google)

users = {"Chavez" : "Isabel Aguillon", "Monch" : "Leonardo Aguillon"}

def getUser (username):
    fullname = users[username]
    return fullname

def login():
    print("Enter Username:")
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
        print("Welcome, " + getUser(user))
    else:
        print("Login Failed")

def getReceiptAmount():
    print("Add Receipt Amount:")
    item = input()
    return item

receiptList = []

amount = "initial"
while len(amount) > 0:
    print("Add another receipt amount or press enter to exit")
    amount = getReceiptAmount()
    if amount != '':
        receiptList.append(amount)

print(receiptList)
print(max(receiptList))
print(min(receiptList))




'''x = (max(receiptList) * 100)
print(x)
y = (min(receiptList) * 100)
print(y)'''







