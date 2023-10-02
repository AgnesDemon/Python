temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)
print(new_temps)

new_temps2 = [temp / 10 for temp in temps]
print(new_temps2)
#Both print out the list divided by ten

numbers = [221, 234, 340, -9999, 230]

#to ignore the -9999:
new_numbers = [number / 10 for number in numbers if number != -9999]
print(new_numbers) #will print new list divided by ten, and -9999 is omitted

#to change -9999 into 0:
new_numbers2 = [number / 10 if number != -9999 else 0 for number in numbers]
print(new_numbers2) #will print new numbers and change -9999 into 0
#new_numbers = [number / 10 for number in numbers if number != -9999 else 0]
#This will not work and will result in an error
