#to change directory, type cd and the address of where you want to go
#in my case, I typed cd .\packt_python\ to run this file

'''myfile = open("fruits.txt")
print(myfile.read()) #note: this will not allow next set of code to work
#prints the output of the .txt file in the terminal
#if you were to execute print(myfile.read()) twice, the file will not be read twice
#instead, it would read it one time, and then create an empty string

#to print the content of the .txt file multiple times:
content = myfile.read()
print(content)
print(content)
#This allows the file to be read more than once

myfile = open("fruits.txt")
content = myfile.read()
myfile.close()
print(content)
#this will open the file, read the content, print the content, and close the file

with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)
#this will open the file, read it, and print it in the terminal, just like the other ones
#the file will close on its own with this function

#say fruits.txt was in a different directory
#you would have to specify which directory and file you want to read
#example, say I have a directory called "Files"
#with open ("Files/fruits.txt") as my file:
#this will allow you to read the file from a different directory

#"r" allows you to read a file
#"w" allows you to write in a file

with open("vegetables.txt", "w") as myfile:
    myfile.write("Tomato")
    myfile.write("\nCucumber\nOnion\n")
    myfile.write("Garlic")

#this creates a new file and adds "Tomato" to the empty file
#if you use this code to an already existing file, the new data will override the old data
#if you wanted to add more lines, then type: myfile.write("Tomato\n")
#you can also add more items: myfile.write("Tomato\nCucumber\nOnion")

#"x" will create a new file and open it for writing
#if file already exists, an error will occur

#what if you want to add to something, not rewrite it completely?
with open("vegetables.txt", "a") as myfile:
    myfile.write("\nOkra")'''
    #file is not readable at this point

#to make file readable:
with open("vegetables.txt", "a+") as myfile:
    myfile.write("\nEggplant")
    myfile.seek(0) #sets the cursor to 0
    #if you don't set the cursor to 0, you will print an empty string
    content = myfile.read()

print(content)
#file is now able to be read