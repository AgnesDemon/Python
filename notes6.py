
#!= means it is not equal to.

#Sudo code example
#Ask user for their email or phone number
#Keep grocery list from user
#Make sure I have an empty list
#Use a while loop to keep collecting groceries
#Ask the user if they are done
#Print the full list when they are done
#Save it to a file, send a text message, send an email, etc.

#while their answer is yes:
    #ask for another item
#Sudo code: putting ideas together and writing them down
#Len means length
#Float allows decimal places
#== means comparing

def getGroceryItem():
    print("Add Item to list:")
    item = input()
    return item

groceryList = []

answer = "initial"
while len(answer) > 0:
    print("Type in a new item to add to the list or press enter to exit")
    answer = getGroceryItem()
    if answer != '':
        groceryList.append(answer)

print(groceryList)
#if answer != '': removed the enter from the list, so it only shows the groceries

#Homework:
#Require proper login with only 3 attempts. If they fail, they will be forced to exit the app
#Receipt calculator - Ask for the amounts, take in x amount of receipts.
#When done, display the rounded total
#Print receipts taken in: line by line, sort list by least to most expensive $xx
#No decimal places because it is rounded
#Bonus items: keep the screen clean (google)
