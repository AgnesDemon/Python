import pandas
import os
import time
clear = lambda: os.system("cls")
import PL_prototype
import getpass

class PL_Login:
    password_info = {"username" : "AgnesDemon", "password" : "Cooper10"}
    
    def login():
        clear()
        sign_in_or_up = input("Welcome to your personal library! To sign in, press 1\nIf you want to sign up, press 2\n")
        if sign_in_or_up == "1":
            clear()
            username = input("Username: ")
            clear()
            #password = input("Password: ")
            password = getpass.getpass("Password: ")
            if username == PL_Login.password_info["username"] and password == PL_Login.password_info["password"]:
                clear()
                input("Welcome, " + PL_Login.password_info["username"] + "! Please enjoy your personal library!\nPress Enter to continue")
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


