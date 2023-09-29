monday_temps = [9.1, 8.8, 7.5]

print(round(monday_temps[0]))
print(round(monday_temps[1]))
print(round(monday_temps[2]))
print("\n")

for temperature in monday_temps:
    print(round(temperature)) #rounds and prints each list item
print("\n")

for letter in 'hello':
    print(letter.title()) #prints each letter in a new line capitalized
print("\n")

student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}
for grades in student_grades.values():
    print(grades) #prints only the grades, or the values in the dictionary
print("\n")

for i in [1, 2, 3]:
    print(i)

'''a = 3
while a > 0:
    print(1)
    print(2)'''
#type Ctrl + C to exit loop

username = ''
while username != "pypy":
    username = input("Enter username: ")
#This loop will continue asking for username until user inputs "pypy"

while True:
    username = input("Enter username: ")
    if username == "pypy":
        break #will stop the code
    else:
        continue #will continue loop until condition is met


