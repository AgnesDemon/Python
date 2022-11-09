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


properties = { 1 : "Intelligence +30%)", 2 : "Fire Resistance +12%", 3 : "Critical Hit Damage +5%", 4 : "Critical Hit Chance +15%", 5 : "Strength +11"}

print("Change Property")
changeProperty = input()
randomProperty = randint(1,5)
print(properties[randomProperty])





