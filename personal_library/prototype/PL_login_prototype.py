import pandas
import os
import time
clear = lambda: os.system("cls")
import PL_prototype
import getpass
import hashlib

#ERROR: missing 3 required positional arguments: 'self', 'username', and 'password'. Need to figure out the problem

class PL_Login:
    #def __init__(self):
        #self.accounts = {}

    #def sign_up(self, username, password):
        #if username in self.accounts:
            #return "Sorry, this username is already in use. Please try again."
        #else:
            #self.accounts[username] = password
            #return "Sign up successful! Enjoy your brand new personal library!"
    
    '''def login(self, username, password):
        clear()
        sign_in_or_up = input("Welcome to your personal library! To sign in, press 1\nIf you want to sign up, press 2\n")
        if sign_in_or_up == "1":
            clear()
            typed_username = input("Username: ")
            clear()
            #password = input("Password: ")
            #typed_password = getpass.getpass("Password: ")
            if typed_username == username in self.accounts: #and self.accounts[username] == password
                clear()
                typed_password = getpass.getpass("Password: ")
                if typed_password == password in self.accounts:
                    input("Welcome, " + self.accounts[username] + "! Please enjoy your personal library!\nPress Enter to continue")
                #time.sleep(2)
                    clear()
                    PL_prototype.Personal_Library.opening()
            else:
                input("Sorry, the information you have typed in is incorrect. Please try again.")
                clear()
                self.login()
        elif sign_in_or_up == "2":
            print("Creating a new account...")'''
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    accounts = {}
    def create_account(username, password):
        if username in PL_Login.accounts:
            print("Username already exists. Please choose a different username.")
        else:
            PL_Login.accounts[username] = PL_Login.hash_password(password)
            print("Account created successfully!")
    def login(username, password):
        if username in PL_Login.accounts and PL_Login.accounts[username] == PL_Login.hash_password(password):
            print("Login successful!")
        else:
            print("Invalid username or password.")
    def main():
        while True:
            print("\n1. Create Account\n2. Login\n3. Exit")
            choice = input("Enter your choice: ")
        
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                PL_Login.create_account(username, password)
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                PL_Login.login(username, password)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    #if __name__ == "__main__":
        #main()
        
#Hashing Passwords: The hash_password function uses SHA-256 to hash passwords for security.
#Account Storage: Accounts are stored in a dictionary where the key is the username and the value is the hashed password.
#Creating Accounts: The create_account function checks if the username already exists and adds the new account if it doesn't.
#Logging In: The login function verifies the username and password by comparing the hashed password.
#User Interaction: The main function provides a simple command-line interface for creating accounts and logging in.


run_function = PL_Login
run_function.main()


