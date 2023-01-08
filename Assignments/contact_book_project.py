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

import csv
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
        print("[Exit]")
        choice = input()
        if choice == "Find contact":
            print("Let's go!")
            
        elif choice == "Create new contact":
            def create_contact():
                clear()
                print("Let's do this!")
                print()
                print("Name:")
                name = input()
                print("Last name:")
                last_name = input()
                print("Address:")
                address = input()
                print("Zip Code:")
                zip_code = input()
                print("City:")
                city = input()
                print("State:")
                state = input()
                print("Email:")
                email = input()
                print("Phone Number:")
                phone_number = input()
                print(name, ",", last_name, ",", address, ",", zip_code, ",", 
                city, ",", state, ",", email, ",", phone_number)
                print()
                print("Save new contact? yes/no")
                response = input()
                if response == "Yes":
                    print("Ok then!")
                    f = open("contact.csv", "a")
                    f.write(name + ", ")
                    f.write(last_name + ", ")
                    f.write(address + ", ")
                    f.write(zip_code + ", ")
                    f.write(city + ", ")
                    f.write(state + ", ")
                    f.write(email + ", ")
                    f.write(phone_number + "\n")
                    f.close()
                elif response == "No":
                    print("Contact was not saved")

            create_contact()

        elif choice == "Delete contact":
            print("Ok, let's go")
        
        elif choice == "See contact list":
            def see_contact_list():
                clear()
                print("Let's see your contacts!")
                print()
                with open("contact.csv") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(" ".join(row))
                #f = open("contact.csv", "r")
                #lines = f.readlines()
                #print(lines)
                
            see_contact_list()
        
        #elif choice == "Exit":
            #clear()
            #print("Thank you, goodbye!")
            #exit()

    intro()

    


#numberLines = len(f.readlines())

#This works:   
#f = open("contact.csv", "r")
#lines = f.readlines()
#print(lines)




