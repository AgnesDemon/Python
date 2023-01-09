import csv
import os
clear = lambda: os.system('cls')


class Navigation:
    def draw_menu(this):
        clear()
        print("Welcome to Contacts! What would you like to do?")
        print("1. Find contact")
        print("2. Create new contact")
        print("3. Delete contact")
        print("4. See contact list")
        print("5. Exit")
        choice = input("Type what you would like to do: ")
        this.handle_choice(choice)
    
    def run(this):
        while True:
            this.draw_menu()

    def handle_choice(this, choice):
        if choice == "5":
            exit("Goodbye!")
        if choice == "2":
            this.create_contact()
        if choice == "4":
            this.see_contact_list()
        if choice == "1":
            filter = input("Type in who you want to find: ")
            search = Contacts()
            contacts = search.find_contacts(filter)
            for contact in contacts:
                print(contact.name)
            this.pause()

    def create_contact(this):
        clear()
        print("Let's do this!")
        print()
        name = input("Name: ")
        last_name = input("Last name: ")
        address = input("Address: ")
        zip_code = input("Zip code: ")
        city = input("City: ")
        state = input("State: ")
        email = input("Email: ")
        phone_number = input("Phone number: ")
        #print(name, ",", last_name, ",", address, ",", zip_code, ",", 
                #city, ",", state, ",", email, ",", phone_number)
        print()
        print("Save new contact? Y/N")
        response = input()
        if response == "Y":
            contact = Contact(name, last_name, address, zip_code, city, state, email, phone_number)
            contact.save()
            print("Contact has been saved!")
        elif response == "N":
            print("Contact was not saved")
    
    def see_contact_list(this):
        clear()
        print("Let's see your contacts!")
        print()
        with open("contact.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                print(" ".join(row))
            this.pause()
    
    def pause(this):
        input("Press Enter to Continue ...")




class Contact:
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
    
    def save(this):
        f = open("contact.csv", "a")
        f.write(f"{this.name},{this.lastname},{this.address},{this.zipcode},{this.city},{this.state},{this.email},{this.phonenumber}\n")
        f.close()
    
class Contacts:
    def find_contacts(this, search):
        f = open("contact.csv", 'r')
        number_lines = len(f.readlines())#Counts number of lines
        f.seek(0, 0)
        starting_line = 0
        contact_list = []
        while starting_line < number_lines:
            current_line = f.readline().strip()
            pieces = current_line.split(",")
            contact = Contact(pieces[0], pieces[1], pieces[2], pieces[3], pieces[4], pieces[5], pieces[6], pieces[7])
            if search.lower() in contact.name.lower():
                contact_list.append(contact)
            starting_line += 1
        return contact_list




        


app = Navigation()
app.run()

        

#contacts = Contacts