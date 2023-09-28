def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
    
print(weather_condition (7))
input("Enter temperature: ")
print(input("Enter temperature: ")) #this will print the input value and the message

'''user_input = input("Enter temperature: ")
print(weather_condition(user_input))'''
#In this case, the input the user gives is turned into a string
#As a result, an error occurs because '>' does not support the instances of str and int
user_input2 = float(input("Enter temperature: "))
print(user_input2)
#Float and int both work
#int cannot convert a float input into an integer


user_input3 = input("Enter your name: ")
message = "Hello %s" % user_input3
print(message)
message2 = f"Hello {user_input3}"
print(message2)
#Both print the same message

#How to add more variables:
name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = "Hello %s %s" % (name, surname)
print(greeting)

greeting2 = f"Hello {name} {surname}"
print(greeting2)
#You can add as many variables as you want
