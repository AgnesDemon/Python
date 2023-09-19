#Chapter 31-32 9-19-2023

'''num = 3
if num >= 3:
    print("Greater than 3")

shape = "square"
if shape == "circle":
    print("you win")
else:
    print("no such luck")

color1 = "red"
color2 = "blue"
if color1 == "red" and color2 == "yellow":
    print("orange")
elif color1 == "red" and color2 == "blue":
    print("purple")
else:
    print("green")

fact = not(5 == 4)
print(fact)'''

'''answer1 = input("Do you want to watch a Harry Potter movie?  ")
if answer1 == "no":
    print("Ok then")
elif answer1 == "yes":
    answer2 = input("Would you like to watch a movie with younger Harry or older Harry?  ")
    if answer2 == "younger":
        print("I would recommend watching movies 1 and 2")
    elif answer2 == "older":
        print("I would recommend watching movies 3 to 7")'''

'''likes_hats = input("Do you like hats?  ")
if likes_hats == "no":
    print("Then you should try out visors!")
elif likes_hats == "yes":
    likes_plain_hats = input("Do you like plain hats?  ")
    if likes_plain_hats == "no":
        print("Then you should try top hats!")
    elif likes_plain_hats == "yes":
        print("Then you should try baseball caps!")'''

'''likes_to_be_bored = input("Do you like to be bored?  ")
if likes_to_be_bored == "yes":
    print("Then do nothing")
elif likes_to_be_bored == "no":
    likes_reading = input("Do you like to read?  ")
    if likes_reading == "no":
        print("Then consider drawing!")
    elif likes_reading == "yes":
        reads_often = input("Do you like to read a lot?  ")
        if reads_often == "yes":
            print("Then you should read a novel!")
        elif reads_often == "no":
            print("Then you should read a magazine!")'''

'''size = input("Is size large?  ")
if size == "no":
    color1 = input("Is color orange?  ")
    if color1 == "no":
        print("Your fish could be tropical")
    elif color1 == "yes":
        print("You probably own a goldfish")
elif size == "yes":
    color2 = input("Is color gray?  ")
    if color2 == "no":
        print("Do you see a whale?")
    elif color2 == "yes":
        print("Look out for sharks!")'''

name = "Max"
def hello_you(person):
    sentence = "Hello" + person
    return sentence
hello_you("Max")
#Return value is: Hello Max

def plotter (x, y):
    instructions = "Plot a course through" + str(x) + " and " + str(y)
    return instructions
plotter(3, 5)
#Return value is: Plot a course through 3 and 5

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return num * -1
absolute_value(-4)
#Return value is: -4 * -1, which equals 4

def favorite(category, thing):
    sentence = "My favorite " + category + "is the" + thing
    return sentence
favorite("snake", "Python")
#Return value is: My favorite snake is the Python