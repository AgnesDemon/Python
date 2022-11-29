#Assignment: File.py
#Allow user to pick the file name
#Check if the file exists and add to it
#If it doesn't exist, create it
#Use a loop and write some numbers to the file
import os
clear = lambda: os.system('cls')

def fileExists(filename):
    try:
        f = open(filename, "r")
        f.close()
        return True
    except:
        print("Cannot open file")
        return False

clear()
print("Enter Filename:")
filename = input()

if fileExists(filename) == True:
    print("File exists! What would you like to add?")
    userText = input()
    f = open(filename, "a")
    f.write(userText + "\n")
    while userText != '':
        print("Add more text or press enter to exit.")
        userText = input()
        f.write(userText + "\n")
        if userText == '':
            f.close()
else:
    print("Creating new file. Add some text:")
    userText = input()
    f = open(filename, "w")
    f.write(userText + "\n")
    while userText != '':
        print("Add more text or press enter to exit.")
        userText = input()
        f.write(userText + "\n")
        if userText == '':
            f.close()


#f = open(filename, 'r')
#f.read()
#f.close()


'''amount = "initial"
if fileExists(filename) == True:
    print("File exists! What would you like to add?")
    userText = input()
    f = open(filename, "a")
    f.write(userText + "\n")
    while len(amount) > 0:
        print("Add more text or press enter to exit.")
        amount = userText
        if amount != '':
            f.close()
    f.close()'''

'''if userText > 0:
    print("Add more text or press enter to exit.")
    elif userText != '':
        exit()'''





