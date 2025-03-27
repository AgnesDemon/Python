import pandas
from prototype import PL_prototype
from PL_prototype import Personal_Library

class PL_Login:
    password_info = {"username" : "AgnesDemon", "password" : "Cooper10"}
    
    def login():
        input("Welcome to your personal library! Please sign in: ")
        username = input("Username: ")
        password = input("Password: ")
        if username == PL_Login.password_info["username"] and password == PL_Login.password_info["password"]:
            print("Welcome, " + PL_Login.password_info["username"] + "! Please enjoy your personal library!")
            Personal_Library.opening()
        else:
            print("Sorry, the information you have typed is incorrect. Please try again.")


