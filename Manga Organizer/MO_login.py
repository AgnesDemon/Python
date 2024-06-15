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
from tkinter import messagebox

window = tkinter.Tk()

window.title("Login") #name of window
window.geometry('340x440') #sets width and height of window
window.configure(bg="#9F9F9F") #sets background color

def login():
    username = "AgnesDemon13"
    password = "11004488"
    if entry1.get() == username and entry2.get() == password:
        #print("Welcome, " + username)
        messagebox.showinfo(title="Login Success", message="You have successfully logged in") #popup that shows you have successfully logged in
        window.destroy()
    else:
        #print("Login failed. Please try again.")
        messagebox.showerror(title="Error", message="Login failed. Please try again.") #popup that shows an error with your login

frame =tkinter.Frame(bg="#9F9F9F")

#Labels
label1 = tkinter.Label(frame, text="Login", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 30))
label1.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) #'sticky=' tells label to take up as much space as possible in said directions 
label2 = tkinter.Label(frame, text="Username", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 16))
label2.grid(row=1, column=0)
label3 = tkinter.Label(frame, text="Password", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 16))
label3.grid(row=2, column=0)

#Entries
entry1 = tkinter.Entry(frame, font=("Arial", 16))
entry1.grid(row=1, column=1, pady=20)
entry2 = tkinter.Entry(frame, show="*", font=("Arial", 16))
entry2.grid(row=2, column=1, pady=20)

#Button
button = tkinter.Button(frame, text="Login", bg="#404040", fg="#FFFFFF", font=("Arial", 16), command=login)
button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()