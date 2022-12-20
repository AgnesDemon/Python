#Naming conventions


#String interpolation - allows the computer to parse the string
name = 'leo'
age = 41

print(name + ' is ' + str(age) + ' years old!')
print(name, 'is', str(age), 'years old!')
print(f"{name} is {age} years old!")

class User:
    first_name = None
    last_name = None

    def __init__(this, first, last):
        this.first_name = first
        this.last_name = last
    
    def get_name(this):
        return f"{this.first_name} {this.last_name}"
    
    def __get_length(thism, data):
        return len(data)
     
user = User("John", "Doe")
#String interpolation while calling a function
print(f"{user.get_name()} was the first user in the system!")

#Snake case applies to variables and functions
first_name = ''
def getfirst_name():
    print(first_name)

#Upper Camel applies to classes  -> Try not to use "lowerCamel" anymore
class PingPong:
    ball = 0

#Constants - ALL UPPER CASE
VELOCITY = 3.14
NUMBER_PLAYERS = 2

#Classes that only a function uses should be prefixed with '__' like "__class_name"
#See User class above

