#Password manager


#Privacy: make sure no one can read the file
#Password database:
    #Name
    #Location
    #Credential Object:
        #Username (email)
        #Password
        #url
        #notes
            #mother maiden name / ...
#Functionality:
    #Create a new password database
    #Check for in use passwords
    #Check password strength
        #Requirements (length, symbols, repeated characters, etc)
    #Create
    #Edit or update
    #Delete
    #Login
        #Use a hidden username or password


#Decise what the basic class is going to look like
#Login
#Encryption - at the end

import password_database as pwdb

menu = {
    1 : "Create a new database",
    2 : "Login to current database",
    3 : "Exit"
}

def handle_choice(choice):
    if choice == "1":
        password_db = pwdb.PasswordDatabase()
        password_db.create_database()
    
    if choice == "3":
        exit("Goodbye!")

choice = "0"
while choice != "3":
    for menuitem in menu:
        print(f"{menuitem}, {menu[menuitem]}")
    choice = input("What would you like to do: ")
    handle_choice(choice)

