import pandas
import os
clear = lambda: os.system("cls")
#import PL_login_prototype

class Personal_Library:
    #may need to make option in beginning where if you have no shelves, Browse Shelves option should not appear
    def opening():
        choice = input("Welcome to your personal library! What would you like to do today?\n1: Browse Shelves\n2: Create new Shelf\n3: Exit Personal Library\n")
        if choice == "1":
            print("Browsing library...")
        elif choice == "2":
            print("Creating new shelf...")
        elif choice == "3":
            Personal_Library.exit()

    def browse():
        browse_choice = input("Which shelf would you like to browse?")
    
    def exit():
        clear()
        y_or_n= input("Are you sure you want to exit? y/n\n")
        if y_or_n == "y":
            clear()
            print("Exiting library...")
        elif y_or_n == "n":
            Personal_Library.opening()

    