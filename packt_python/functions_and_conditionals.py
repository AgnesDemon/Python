def mean(mylist):
    print("Function started!")
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5])) #this will print the mean
print("\n")
#If you don't return a value or type return None,
#the term None would be printed in the terminal

#To make a function process both lists and dictionaries:
def mean2(value):
    #if isinstance(value, dict): works too in place of next line
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
print(mean2(monday_temperatures))
student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}
#print(mean(student_grades)) #This will cause an error
print(mean2(student_grades))
print("\n")

x = 3
y = 1
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")

