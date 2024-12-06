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