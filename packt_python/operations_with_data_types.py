monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(8.1) #adds item to list
print(monday_temperatures)

#to find what a certain function does: help(class.function)
#Example: help(list.append)

index = monday_temperatures.index(8.8)
print(index)
#In this case, the print value is 1, because the list starts at 0
#8.8 is the second value, but since list starts at 0, 8.8 would be 1

#How to get an item given its index:
item = monday_temperatures.__getitem__(1)
print(item)
#or
item2 = monday_temperatures[1]
print(item2)
#Both result in 8.8

monday_temperatures.clear() #clears list
print(monday_temperatures)

tuesday_temperatues = [9.1, 8.8, 7.5, 6.6, 9.9]
length = len(tuesday_temperatues)
print(length) #prints how many values are in the list

tues_item = tuesday_temperatues[3]
print(tues_item) #prints the item called

portion = tuesday_temperatues[1:4]
print(portion) #prints selected portion of list except last item
#tuesday_temperatures[0:4] or tuesday_temperatures[:4]
#These will give you the same results. Both will start at 0

portion2 = tuesday_temperatues[3:5]
print(portion2) #will print [6.6, 9.9]
#This is because there is no item 5 since the list starts at 0
#So it just prints to the last value
#tuesday_temperatures[3:] will print the same thing
#If you put negative numbers, it will print the listed items backwards
#For example: tuesday_temperatues[-1] will print the last item
#tuesday_temperatures[-4] will print the first item
#You can do this to strings as well, not just integers and floats
#Dictionaries use keys as indexes
#Lists use numbers as indexes



