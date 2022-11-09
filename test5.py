from random import randint

#if statements
age = 14
if age < 21:
    cantSmoke = True
elif age > 65:
    cantSmoke = False
else:
    cantSmoke = True

#You can put any or multiple conditions in a while loop
#print() makes an empty line
#input() allows you to type something in the terminal
#append allows you to add something to a list
'''
name = "John"
while (name != "Monch") and (name != "Chavez"):
    print("You're not one of my children")
'''
#random number functions
messages = { 1 : "Not Today", 2 : "Try Again Later", 3 : "Definitely Not", 4 : "There's a Chance", 5 : "Yes"}

print("What's your question?")
question = input()
randomNumber = randint(1,5)
#print(randomNumber)
print(messages[randomNumber])

def getNumbers(numbers):
    numbersToReturn = []
    i = 0
    while i < numbers:
        numbersToReturn.append(randint(1,65))
        i += 1
    return numbersToReturn

def playPowerball():
    print("here are your lucky numbers:")
    numbers = getNumbers(5)
    print(numbers)

playPowerball()

#boolean values are basically true and false statements.
evenNumberList = ["0", "2", "4", "6", "8"]
myNumber = 80

def modIsEven(num):
    modValue = num % 2
    if modValue > 0:
        return False
    return True

def isEven(num):
    mynum = str(num)
    print(mynum[-1])
    lastDigit = mynum[-1]
    if lastDigit in evenNumberList:
        return True
    return False

print(isEven(myNumber))
print(modIsEven(myNumber))
