#9-26-2023
spent = 3
donated = 4
total_amount = spent + donated
print(total_amount)

items = 10
price = 2
total_price = items * price
print(total_price)

#You can use the terminal to write throw-away code for quick tests
#Python interactive shell is also the terminal
#If you have an error and you see three arrows, type exit() and the terminal should go back to normal
#To open the python interactive shell in Windows, type py -3
#To exit the python interactive shell, use exit()
#To clear the terminal in Windows, type cls

x = 10 #integer
y = "10" #string
z = 10.1 #float
sum1 = x + x
sum2 = y + y
print(sum1, sum2)
print(type(x), type(y), type(z)) #this prints each variable type

#You can put strings, integers, floats, and even another list within a list
example1 = ["10", 9, 8.8, [7.5, 4, 6]]
print(example1)

example2 = range(0, 11)
print(example2)
#This will print "range(0,11)"

example3 = list(range(0, 11))
print(example3)
#This will print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

example4 = list(range(1, 9, 2))
print(example4)
#This will print [1, 3, 5, 7]
#The range starts at one, counts by 2, and ends by 9.

#You can use the python interactive shell to find functions
#You can do this by typing dir((str, float, int, list, etc))

student_grades = [9.1, 8.8, 7.5]
my_sum = sum(student_grades)
length = len(student_grades)
mean = my_sum / length
print(mean)
#This prints the mean value of the list student_grades

#Curly brackets are used for dictionaries
student_grades2 = {"Mary" : 9.1, "Sam" : 8.8, "John" : 7.5}
my_sum2 = sum(student_grades2.values())
print(student_grades2.values())
#This will print the values of the dictionary, or in this case, the grades
print(my_sum2)
print(student_grades2.keys())
#This will print the keys of the dictionary, or in this case, the names

#Tuple: a list but with parenthesis
monday_temp = (1, 4, 5)
print(monday_temp)
#Tuples don't have an append method

