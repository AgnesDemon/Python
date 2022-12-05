#Assignment
#add up each bill separately (like running total)
#create a new script that will ad 25 random rows to test.csv
#example: total phone, total house, total food, etc.
#Fileprocessing.py

#csvGenerator.py
import os
clear = lambda: os.system('cls')

class Bills:
    def __init__(this, name, phone, house, electric, water, food):
        this.name = name
        this.phone = phone
        this.house = house
        this.electric = electric
        this.water = water
        this.food = food

    def total(this):
        return this.phone + this.house + this.electric + this.water + this.food

def savetoFile(name, total):
    filename = 'total.txt'
    f = open(filename, 'a')
    f.write(name + ": " + str(total) + "\n")
    f.close()


def clearFile():
    filename = 'total.txt'
    f = open(filename, 'w')
    f.close() 

clear()
clearFile() # using this to clear out our save file 

f = open("test.csv", "r") 
numberLines = len(f.readlines()) 
f.seek(0,0)
startingLine = 0 
runningTotal = 0
recordsProcessed = 0
totalPhone = 0
totalHouse = 0
totalElectric = 0
totalWater = 0
totalFood = 0

while startingLine < numberLines:
    line = f.readline() 
    line = line.strip() 
    pieces = line.split(',')
    cleanPieces = []
    for piece in pieces:
        cleanPieces.append(piece.strip())
    if str(cleanPieces[1]).isdigit():
        userBills = Bills(cleanPieces[0], int(cleanPieces[1]), int(cleanPieces[2]), int(cleanPieces[3]), int(cleanPieces[4]), int(cleanPieces[5]))
        print(userBills.name, ": ", userBills.total())
        savetoFile(userBills.name, userBills.total())
        runningTotal += int(userBills.total())
        recordsProcessed += 1
        totalPhone += int(userBills.phone)
        totalHouse += int(userBills.house)
        totalElectric += int(userBills.electric)
        totalWater += int(userBills.water)
        totalFood += int(userBills.food)
    else:
        print("skipped: ", line)
    #print(userBills.electric)
    '''for piece in pieces: #looping through the split apart pieces
        piece = piece.strip() #using strip to clean off empty spaces
        print(piece)'''
    startingLine += 1

print()
print("Records Processed: ", recordsProcessed)
print("Running Total: ", runningTotal)
print()
print("Total Phone: ", totalPhone)
print("Total House: ", totalHouse)
print("Total Electric: ", totalElectric)
print("Total Water: ", totalWater)
print("Total Food: ", totalFood)

