#Assignment
#Display three properties
#Allow user to change one of the properties using the key
#System will generate a random property and display 3 properties again
'''
initial properties will be randomly generated
1 strength
2 armor
3 resistance

Which property would you like to change?
1

1 life steal
2 armor
3 resistance

loop until user is satisfied

'''
#My 3 properties: Strength +15, Resistance to All Elements +20%, Critical Hit Chance +12%

from random import randint

'''originalPowersList = ["1: Strength +15", "2: Resistance to All Elements +20%", "3: Critial Hit Chance +12%"]
for power in originalPowersList:
    print(power)

properties = { 1 : "Intelligence +30%", 2 : "Fire Resistance +12%", 3 : "Critical Hit Damage +5%", 4 : "Critical Hit Chance +15%", 5 : "Strength +11"}

print("Which power would you like to change?")
changeProperty = input()
randomProperty = randint(1,5)
print("Here is your new power: " + properties[randomProperty])'''
#Basic version, works, but does not contain certain tasks




'''originalPowersList = {1 : "Strength", 2 : "Resistance to All Elements", 3 : "Critical Hit Chance"}
for power in originalPowersList:
    print(power)'''


originalPowersList = {1 : "Strength", 2 : "Resistance to All Elements", 3 : "Critical Hit Chance"}
def oP():
    for power in originalPowersList:
        print(power, originalPowersList[power])


properties = {1 : "Intelligence", 2 : "Fire Resistance", 3 : "Critical Hit Damage", 4 : "Critical Hit Chance", 5 : "Strength"}
def powerChange ():
    print("Which power would you like to change?")
    changeProperty = input()
    randomProperty = randint(1,5)
    print("Here is your new power: " + properties[randomProperty])
    originalPowersList [changeProperty] = properties[randomProperty]

oP()
powerChange()







