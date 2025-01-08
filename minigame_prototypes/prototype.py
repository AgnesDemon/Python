import pandas
import os
clear = lambda: os.system('cls')

#PRINTS OUT ALL LINES AT THE SAME TIME IN THEIR OWN LINE, NOT WHAT I WANT
'''with open("sampletext.txt", "r") as file:
    for line in file:
        print(line.strip())'''

#PRINTS OUT ALL LINES AT THE SAME TIME IN THEIR OWN LINE, THIS TIME SHOWING THEIR LINE NUMBER, NOT WHAT I WANT
'''file = open('sampletext.txt', 'r')
count = 0
for line in file:
    count += 1
    print("Line {}: {}".format(count, line.strip()))
file.close()'''

#CAN PRINT LINES ONE AT A TIME AND CLEARS TERMINAL BEFORE EACH SENTENCE, THIS ONE MAY WORK
with open('sampletext.txt', 'r') as file:
    line = file.readline()
    while line:
        #print(line.strip())
        clear()
        input(line.strip())
        line = file.readline()

'''file = open("sampletext.txt", 'r')
dictionary = {}
for line in file:
    key, value = line.strip().split('=')
    dictionary[key.strip()] = value.strip()
file.close()'''

#EXAMPLE
'''my_dictionary = {}
index = 0
with open("sampletext.txt", 'r') as file:
    for line in file:
        index = index + 1
        my_dictionary[index] = line.strip()
print(my_dictionary)
print(index)'''

dictionary = {}
index = 0
with open("sampletext.txt", 'r') as file:
    for line in file:
        index = index + 1
        dictionary[index] = line.strip()
for key in dictionary:
    print(f"{key} : {dictionary[key]}")
    #input(f"{key} : {dictionary[key]}")



