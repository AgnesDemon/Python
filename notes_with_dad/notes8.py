#Objects / Classes
"""class Person0:
    age = 0
    name = ""
    height = 0
    lastName = ""

class PersonA:
    age = 41
    name = "Leonard"
    height = 68
    lastName = "Aguillon"

person = PersonA()
print(person.name, person.lastName)


class PersonB:
    def __init__(self, age, name, height, lastName):
        self.age = age
        self.name = name
        self.height = height
        self.lastName = lastName

person1 = PersonB(41, "Leonard", 68, "Aguillon")
if (person1.age > 21):
    print(person1.name, "is old enough to drink")

person2 = PersonB(33, "Olivia", 60, "Aguillon")

class Bills:
    #__int__ is the class constructor
    #When data is passed to it, it assigns the given data to the associated properties of the class
    def __init__(self, rent, electric, water, gas, phone):
        self.rent = rent
        self.electric = electric
        self.water = water
        self.gas = gas
        self.phone = phone
    
    #Defining a function inside the class
    def total(self):
        return(self.rent + self.electric + self.water + self.gas + self.phone)
    
    #Calling a function from another function
    def yearlyTotal(self):
        return self.total()* 12


leoBills = Bills(1350, 250, 100, 0, 115)
leosTotal = leoBills.total()
print(leosTotal)
print(leoBills.yearlyTotal())
#You can name "self" anything you want. It doesn't have to say "self"

class Pizza:
    def __init__(this, size, crust, toppings):
        this.Size = size
        this.Crust = crust
        this.Toppings = toppings

pizza = Pizza("Large", "Stuffed Crust", ["Pepperoni, Jalapeno, Mushroom"])
print(pizza.Toppings)"""


#Files - Saving, reading, writing data
#A file is a collection of data
#db - text file
#PNG - image file

'''file = open("test.txt", "r")
print(file.read())'''
#It doesn't work because there is no "test.txt"

'''file = open("test7.py", "r")
print(file.read())
#It worked because there is a "test7.py" file
#File open command - uses the current directory where the script is being run from
print(file.read(6))
#Prints out however many characters asked for
print(file.readline())
#Allows a line to be read; looks for a line terminator or end of line characters like 'enter'
print(file.readline())
print(file.readline())
#Reads two separate lines
file.seek(0, 0)
file.close()

#File writing
f = open("test.txt", "w")
#"w" means write and it will overwrite the file contents
f.write("Hello world.")
f.close()

f = open("test.txt", "a")
#"a" is append and will add data to a file
f.write("Hello people.")
f.close()
#It puts the new words right next to the first words; it does not create a new line

f = open("test.txt", "w")
f.write("Hello world.\n")
f.close()

f = open("test.txt", "a")
f.write("Hello people.\n")
f.close()
#\n adds a new line, or an enter, to the line'''


#File check if file exists
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

f = open(filename, 'r')
f.read()
f.close()


#Assignment: File.py
#Allow user to pick the file name
#Check if the file exists and add to it
#If it doesn't exist, create it
#Use a loop and write some numbers to the file

