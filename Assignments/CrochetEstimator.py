#Important things for crochet:
    #Yarn
    #Number of hours
    #Whether or not I used a paid pattern

#I need to calculate the cost of the yarn, the hourly rate, and the pattern cost
#Need to note that I use more than one color or type of yarn
#Hourly rate is most likely going to be at least $12
#I can make it to where I can type in my own hourly rate
#Should probably allow a pattern to equal $0, since not all patterns are costly
#Should also probably consider that I may use more than one pattern




import os
clear = lambda: os.system('cls')

class Amount:
    patterns = 0
    yarn_skeins = 0
    number_of_hours = 0

    def __init__(this, Patterns, Yarn_Skeins, Hours):
        this.patterns = Patterns
        this.yarn_skeins = Yarn_Skeins
        this.hours = Hours


class Cost:
    pattern = 0
    yarn = 0
    hourly_rate = 0

    def __init__(this, Pattern, Yarn, Hourly_Rate):
        this.pattern = Pattern
        this.yarn = Yarn
        this.hourly_rate = Hourly_Rate

