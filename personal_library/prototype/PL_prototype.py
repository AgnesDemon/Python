import pandas
import os
clear = lambda: os.system("cls")
import PL_login_prototype
from PL_login_prototype import PL_Login
#import PL_login_prototype

#to create a folder using python:
    #make sure os is imported
    #directory = "new_folder"
    #os.makedirs(directory, exist_ok = True)
    #to make sure it worked, "print(f"Directory '{directory}' created successfully!")"

class Personal_Library:
    #may need to make option in beginning where if you have no shelves, Browse Shelves option should not appear
    def opening():
        choice = input("What would you like to do today?\n1: Browse Shelves\n2: Create new Shelf\n3: Exit Personal Library\n")
        if choice == "1":
            print("Browsing library...")
        elif choice == "2":
            print("Creating new shelf...")
        elif choice == "3":
            Personal_Library.exit()

    def browse():
        browse_choice = input("Which shelf would you like to browse?")

    def create_new_shelf():
        shelf_name = input("What would you like to name your shelf?\n")
        
    
    def exit():
        clear()
        y_or_n= input("Are you sure you want to exit? y/n\n")
        if y_or_n == "y":
            clear()
            print("Exiting library...")
        elif y_or_n == "n":
            Personal_Library.opening()
        else:
            clear()
            input("I'm sorry, I didn't understand your answer. Please type in your answer again.")
            Personal_Library.exit()


#this works
'''directory = "AgnesDemon_library"C
os.makedirs(directory, exist_ok=True)
print(f"Directory '{directory}' created successfully!")'''

#DIFFERENT WAYS TO ACCESS FILES IN SEPARATE FOLDERS:
'''import os

folder = "folder"
filename = "filename.txt"
file_path = os.path.join(folder, filename)

with open(file_path, 'r') as file:
    content = file.read()
    print(content)'''

'''file_path = "../folder/filename.txt"  # Adjust the path as needed

with open(file_path, 'r') as file:
    content = file.read()
    print(content)'''

