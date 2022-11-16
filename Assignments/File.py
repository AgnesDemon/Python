#Assignment: File.py
#Allow user to pick the file name
#Check if the file exists and add to it
#If it doesn't exist, create it
#Use a loop and write some numbers to the file


def fileExists(filename):
    try:
        print(filename)
        f = open(filename, "r")
        f.close()
        return True
    except:
        print("Failing to open file")
        return False


print("Enter Filename:")
filename = input()

if fileExists(filename) == True:
    print("File exists, what would you like to add?")
    userText = input()
    f = open(filename, "a")
    f.write(userText + "\n")
    f.close()
else:
    print("Creating new file, Add some text:")
    userText = input()
    f = open(filename, "w")
    f.write(userText + "\n")
    f.close()

#f = open(filename, 'r')
#f.read()
#f.close()







