#Contact Book Project

#Show total number of contacts, maybe show first x amount.
#What would you like to do?
    #Search for contact
        #Search by first name
    #Add new contact
        #Probably allow for blank data
    #Edit contact
        #What will the edit screen look like, maybe ask them what they want to edit
    #Display Contact
        #Shows all contacts
            #Allow user to pick a user id to show a specific contact
    #Remove contact
        #Probably should confirm they really want to do this
        #How do we decide who to remove

#Contact:
    #First name
    #Last name
    #Address
    #Zip code
    #State
    #City
    #Email
    #Phone

#Adding would save the record in some fashion, maybe CSV

#Example: Isabel, Aguillon, 14114 Wetmore Bend, San Antonio, TX, 78247, chavelina0105@gmail.com, 210-725-0262


#Need to use input to allow the user to type in the contact.
#Need to save the input
#Maybe use a loop as the user types the information and allows them to just press enter if they don't know certain information.


import os
clear = lambda: os.system('cls')

class Contacts:
    name = None
    lastname = None
    address = None
    zipcode = None
    city = None
    state = None
    email = None
    phonenumber = None

    def __init__(this, Name, Last_Name, Address, Zip_Code, City, State, Email, Phone_Number):
        this.name = Name
        this.lastname = Last_Name
        this.address = Address
        this.zipcode = Zip_Code
        this.city = City
        this.state = State
        this.email = Email
        this.phonenumber = Phone_Number

    def intro():
        clear()
        print("Welcome to Contacts! What would you like to do?")
        print("[Find contact]")
        print("[Create new contact]")
        print("[Delete contact]")
        print("[See contact list]")
        choice = input()
        if choice == "Find contact":
            print("Let's go!")
            
        elif choice == "Create new contact":
            def create_contact():
                clear()
                print("Let's do this!")
                print("Name:")
                name = input()
                return name
            create_contact()

        elif choice == "Delete contact":
            print("Ok, let's go")
        
        elif choice == "See contact list":
            print("Let's see your contacts!")
            def see_contact_list():
                f = open("contact.csv", "r")
                lines = f.readlines()
                print(lines)
                
            see_contact_list()


    intro()

    contact_list = []


#numberLines = len(f.readlines())
    





