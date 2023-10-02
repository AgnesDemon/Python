#the len() function only takes in one argument, which is object
#the isinstance() function takes in two arguments
#these two arguments that the function takes are objects and class or tuples
#if you try to put more than 1 argument in len(), error will occur
#if you try to put 1 or 3 or more arguments in isinstance(), error will occur
#print() can take an indefinite number of arguments

def area (a, b):
    return a * b
print(area(4, 5)) #prints the area
#(4, 5) are non keyword arguments because they don't have keywords attached to them
#However, if they were assigned like this: (a=4, b=5), then they would be considered keywords

#a parameter could have a default value
#example: def area (a, b=6):
#in this example, you would not have to set a paramter for b
#in this example, a could still be a keyword or non-keyword argument
#for some reason you can, but don't have to, set a parameter for b

#note: a default parameter cannot be before non-default parameters

def mean(*args):
    return args
print(mean(1, 3, 'a', 4))
#prints a tuple containing all the objects in the code
#you cannot put in keywords

#to allow to put in keywords:
def mean2(**kwargs):
    return kwargs
print(mean2(a=1, b=2, c=3))
#prints a dictionary
