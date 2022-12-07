#Homework:
#Create a class; give descriptive name, 5 properties, create the constructor.
#Bonus: create a few instances of your class and loop through them.

class Crochet:
    Project = 0
    Yarn = 0
    CrochetTools = 0
    Eyes = 0
    Hours = 0
    Pattern = 'y'

    def __init__(this, project, yarn, tools, eyes, hours, patterns = 'y'):
        this.Project = project
        this.Yarn = yarn
        this.CrochetTools = tools
        this.Eyes = eyes
        this.Hours = hours
        this.Pattern = patterns

crochetBag = Crochet('Bag', 4, 30, 1, 6, 'y')
#print("Crochet Bag yarn costs: ", crochetBag.Yarn)
crochetSchnauzer = Crochet('Schnauzer', 4, 30, 1, 7, 'y')
crochetFrog = Crochet('Frog', 2, 30, 1, 6, 'y')
crochetDoll = Crochet('Doll', 8, 30, 0, 10, 'y')

crochetProjects = [crochetBag, crochetSchnauzer, crochetFrog, crochetDoll]

for project in crochetProjects:
    if project.Hours > 7:
        print(project.Project, "is at least $90.")
    if project.Yarn > 4:
        print(project.Project, "uses a lot of yarn.")


#Homework
#create a class that helps you calculate something



