class House:
    Owner = 0
    SquareFootage = 0
    Bedrooms = 0
    Bathrooms = 0
    NumberStories = 0
    AttachedGarage = 'y'
    Basement = 'n'

    def __init__(this, sqFeet, bedrooms, bathrooms, stories, garage = 'y', basement = 'n'):
        this.SquareFootage = sqFeet
        this.Bedrooms = bedrooms
        this.Bathrooms = bathrooms
        this.NumberStories = stories
        this.AttachedGarage = garage
        this.Basement = basement

bolisHouse = House('Olivia Aguillon', 2650, 3, 2.5, 2, 'y', 'n')
#print("bolis house is: ", bolisHouse.SquareFootage, "sqft")


leosHouse = House('Livier Aguillon', 2381, 3, 2.5, 2)
isasHouse = House('Isabel Aguillon', 327, 1, 1, 2, 'n', 'n')
donaldsHouse = House('Donald Martin', 3700, 4, 4.5, 3, 'y', 'n')

houses = [bolisHouse, leosHouse, isasHouse, donaldsHouse]

for house in houses:
    if house.Bedrooms > 2:
        print(house.Owner, "has an awesome house!")
    if house.SquareFootage < 400:
        print(house.Owner, "has an awesome electric bill!")



#Homework:
#Create a class; give descriptive name, 5 properties, create the constructor.
#Bonus: create a few instances of your class and loop through them.



