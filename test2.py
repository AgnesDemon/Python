
from re import X


mystring = "78247-4114"
print(mystring[3])

mystring = "78247-4114"
print(mystring[0:5])

mystring = "Hello World"
print(mystring[2:6])

print(mystring[1])  # first character
print(mystring[-1])  # last character
print(mystring[0:5])  # range of characters.

# lists
pets = ['cat','dog','fish','gerbil']
#pets = (17,'fish',"dog",1000.00)
print(pets)
print(pets[-2])
print(pets[1:2])

# tuple
dogs = ['german shepherd','golden retriever','boxer','yorkie']
#dogs[0] = 'pitbull' throws error, tuples cannot be updated
print(dogs[0])
#print(dogs)
#print(dogs[-2])
#print(dogs[1:2])


# Dictionary is a set of key value pairs
#webster = {} means empty dictionary
webster = {}
webster[0] = '0'
webster[1] = '1'
webster['a'] = 'a'
print(webster)

webster[0] = '0 value'
print(webster[0])

'''webster = {'cat':'cute','dog':'happy'}
print(webster)
print(webster['a'])'''


# loops for loop, while loop
# For loop means to do something while the condition is true; it is usually tied to a fixed number of times
pets = ['cat','dog','fish','gerbil']
for pet in pets:
    print(pet)

x = 0
while (x < 10):
    x = x + 1
    print(x)

x = 0
i = 0
while (x < 10):
    x = x + 1
    i = x
    print(x * i)

# make a 10x10 Cube, any character, but it must use loops

#while(True):
    #print("hello")
# Press Ctrl + C to stop
