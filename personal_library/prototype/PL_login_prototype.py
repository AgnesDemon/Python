import pandas
import os
clear = lambda: os.system("cls")
#import getpass
import pwinput

#Notes:
    #need to make sure after logging in or creating a new password, it goes into the user's directory folder, or their "library"
    #need to allow user to open whichever folder (or "shelf") they want to open in their library and be able to view it in the terminal
    #need to allow user to create new folders, or "shelves"
    #may need to either change directory so that user can access their "library"
    #can also call something from their library without having to change directory ("personal_library\prototype\AgnesDemon_library\books.txt")
    #I may be able to put a class within a class to help with changing directory

class PL_Login:
    def read_user_logins():
        with open('users.txt', 'r') as f:
            contents = f.readlines()
            #print(contents)
            #['AgnesDemon,Cooper10\n', 'DummyUsername,DummyPassword'] - this is what it prints out

            new_contents = []
            for line in contents:
                fields = line.split(',')
                fields[1] = fields[1].rstrip() #.rstrip - removes last character in a string. This helps get rid of \n at end of line
                new_contents.append(fields)
            return new_contents
    
    logins = read_user_logins()
    
    def login():
        clear()
        typed_username = str(input("Username: "))
        clear()
        #typed_password = str(getpass.getpass("Password: "))
        typed_password = str(pwinput.pwinput(prompt="Password: ", mask="*")) #when password is typed, asterisks are shown instead for security reasons
        logged_in = False
        for line in PL_Login.logins:
            if line[0] == typed_username and logged_in == False:
                if line[1] == typed_password:
                    logged_in = True
        if logged_in == True:
            clear()
            input("Welcome, " + typed_username + "! Please enjoy your personal library!")
            clear()
            #need to change directory here?
            Personal_Library.opening()
        else:
            input("Sorry, the username or password is incorrect. Please try again.\nPress Enter to retry.")
            PL_Login.login()
    
    def create_new_account():
        clear()
        new_username = input("Type in your username: ")
        new_password = input("Type in your password: ")
        f = open("users.txt", 'a') #opens users.txt file
        f.write('\n' + new_username + ',' + new_password) #adds new username and password to users.txt
        f.close()
        directory = new_username + "_library" 
        os.makedirs(directory, exist_ok=True) #creates directory, or "library"
        #input(f"Folder '{directory} created successfully!")
        clear()
        input("Welcome, " + new_username + "! Please enjoy your personal library!")
        #need to change directory here?
        Personal_Library.opening()

    def exit():
        clear()
        y_or_n= input("Are you sure you want to exit? y/n\n")
        if y_or_n == "y":
            clear()
            print("Exiting...")
        elif y_or_n == "n":
            PL_Login.main()
        else:
            clear()
            input("I'm sorry, I didn't understand your answer. Please type in your answer again.")
            PL_Login.exit()

    def main():
        clear()
        sign_in_or_up = input("Welcome to your personal library!\nIf you already have an account, press 1 to log in.\nIf you want to create a new account, press 2.\nIf you wish to exit, press 3.\n")
        if sign_in_or_up == "1":
            PL_Login.login()
        elif sign_in_or_up == "2":
            PL_Login.create_new_account()
        elif sign_in_or_up == "3":
            PL_Login.exit()

#at the moment this is in a loop. Need to fix this  -- PERSONAL NOTE: can't find said loop, maybe I fixed it?

class Personal_Library:
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


run_function = PL_Login
run_function.main()

#this works
'''directory = "AgnesDemon_library"C
os.makedirs(directory, exist_ok=True)
print(f"Directory '{directory}' created successfully!")'''

#to create a folder using python:
    #make sure os is imported
    #directory = "new_folder"
    #os.makedirs(directory, exist_ok = True)
    #to make sure it worked, "print(f"Directory '{directory}' created successfully!")"


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

    #def __init__(self):
        #self.accounts = {}

    #def sign_up(self, username, password):
        #if username in self.accounts:
            #return "Sorry, this username is already in use. Please try again."
        #else:
            #self.accounts[username] = password
            #return "Sign up successful! Enjoy your brand new personal library!"

            
        
'''def hash_password(password):
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

    print(accounts)

    def main():
        while True:
            print(PL_Login.accounts)
            print("\n1. Create Account\n2. Login\n3. Exit")
            choice = input("Enter your choice: ")
        
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                PL_Login.create_account(username, password)
            elif choice == '2':
                username = input("Enter username: ")
                password = getpass.getpass("Enter password: ")
                PL_Login.login(username, password)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")'''
#Hashing Passwords: The hash_password function uses SHA-256 to hash passwords for security.
#Account Storage: Accounts are stored in a dictionary where the key is the username and the value is the hashed password.
#Creating Accounts: The create_account function checks if the username already exists and adds the new account if it doesn't.
#Logging In: The login function verifies the username and password by comparing the hashed password.
#User Interaction: The main function provides a simple command-line interface for creating accounts and logging in.
