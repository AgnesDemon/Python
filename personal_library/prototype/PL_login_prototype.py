import pandas
import os
import time
clear = lambda: os.system("cls")
import PL_prototype

class PL_Login:
    password_info = {"username" : "AgnesDemon", "password" : "Cooper10"}
    
    def login():
        clear()
        input("Welcome to your personal library! To sign in, press enter to continue")
        clear()
        username = input("Username: ")
        clear()
        password = input("Password: ")
        if username == PL_Login.password_info["username"] and password == PL_Login.password_info["password"]:
            input("Welcome, " + PL_Login.password_info["username"] + "! Please enjoy your personal library!\nPress Enter to continue")
            #time.sleep(2)
            clear()
            PL_prototype.Personal_Library.opening()
        else:
            input("Sorry, the information you have typed is incorrect. Please try again.")
            clear()
            PL_Login.login()

run_function = PL_Login
run_function.login()


