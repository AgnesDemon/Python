#TERMINAL LOGIN

import os
clear = lambda: os.system('cls')

'''users = {"AgnesDemon13" : "Agnes"}

def get_user (username):
    name = users[username]
    return name

def login():
    print("Welcome to your local Manga Organizer! Please enter your username: ")
    username = input()
    clear()
    return username

def check_user(username):
    if username in users:
        return True
    else:
        return False

logged_in = False
while logged_in == False:
    user = login()
    valid_user = check_user(user)
    if valid_user:
        logged_in = True
        print("Welcome, " + get_user(user))
    else:
        print("Invalid login. Please try again.")'''


#GRAPHIC UI LOGIN



import tkinter
#from tkinter import messagebox

window = tkinter.Tk()

window.title("Login") #name of window
window.configure(bg="#9F9F9F") #sets background color

#Labels
label1 = tkinter.Label(window, text="Login", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 30))
label1.grid(row=0, column=0, columnspan=2)
label2 = tkinter.Label(window, text="Username", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 20))
label2.grid(row=1, column=0)
label3 = tkinter.Label(window, text="Password", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 20))
label3.grid(row=2, column=0)

#Entries
entry1 = tkinter.Entry(window)
entry1.grid(row=1, column=1)
entry2 = tkinter.Entry(window, show="*")
entry2.grid(row=2, column=1)

#Button
button = tkinter.Button(window, text="Login", bg="#404040", fg="#FFFFFF")
button.grid(row=3, column=0, columnspan=2)

window.mainloop()