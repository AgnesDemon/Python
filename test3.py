from filecmp import cmp
from math import ceil, floor

'''
loops = 100
x = 1

while x <= loops:
    x += 1
    print("X" * (loops))

#math functions
absolutevalue = abs(-7)
print(absolutevalue)

#absolute value is the distance from zero
'''

ceilValue = ceil(99.87)
print(ceilValue)
#ceil is not rounding; always goes up

floorValue = floor(99.99) 
print(floorValue)
#floor always goes down

#cmp is short for compare
compareValue = cmp(1,2)
print(compareValue)
#true if the same; false if not the same

#other function exp(exponent of), log(logarithm of), log10(logarithm of base 10)
#max(item1, item2), min(item1, item2), sqrt(square root), round(value, places)

#Functions
def printMe (str):
    print (str)
    return

def multiply (intA, intB):
    answer = intA * intB
    print(answer)
    return answer

printMe("hello world")

x = multiply(9, 10)
print(x * 10)

print(max(100,200))
print(min(100,200))

