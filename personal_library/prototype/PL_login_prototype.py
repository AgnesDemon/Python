import pandas
import os
import time
clear = lambda: os.system("cls")
import PL_prototype
import getpass

#ERROR: missing 3 required positional arguments: 'self', 'username', and 'password'. Need to figure out the problem

class PL_Login:
    def __init__(self):
        self.accounts = {}

    def sign_up(self, username, password):
        if username in self.accounts:
            return "Sorry, this username is already in use. Please try again."
        else:
            self.accounts[username] = password
            return "Sign up successful! Enjoy your brand new personal library!"
    
    def login(self, username, password):
        clear()
        sign_in_or_up = input("Welcome to your personal library! To sign in, press 1\nIf you want to sign up, press 2\n")
        if sign_in_or_up == "1":
            clear()
            username = input("Username: ")
            clear()
            #password = input("Password: ")
            password = getpass.getpass("Password: ")
            if username in self.accounts and self.accounts[username] == password:
                clear()
                input("Welcome, " + self.accounts[username] + "! Please enjoy your personal library!\nPress Enter to continue")
                #time.sleep(2)
                clear()
                PL_prototype.Personal_Library.opening()
            else:
                input("Sorry, the information you have typed in is incorrect. Please try again.")
                clear()
                PL_Login.login()
        elif sign_in_or_up == "2":
            print("Creating a new account...")
        



run_function = PL_Login
run_function.login()


