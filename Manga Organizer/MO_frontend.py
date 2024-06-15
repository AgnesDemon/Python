#Should be able to log in
#Should be able to create folders for different manga series
#Should be able to add and store new manga into files
#Should organize manga in order by volume
#Volumes should include names, volume numbers, and authors
#Should be able to see the files
#Maybe delete files or manga
#Make sure I cannot make duplicates. This means that the manga can have the same name, but not the same volume number
from tkinter import *
import MO_login
from MO_backend import Database

database = Database("personal_manga_library.db") #name of .db file

def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)

    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])

def view_command():
    list_box.delete(0, END)
    for row in database.view_all_manga():
        list_box.insert(END, row)

def search_command():
    list_box.delete(0, END)
    for row in database.search_volume(manga_name_text.get(), volume_number_text.get(), author_text.get()):
        list_box.insert(END, row)

def add_command():
    database.insert(manga_name_text.get(), volume_number_text.get(), author_text.get())
    list_box.delete(0, END)
    list_box.insert(END, (manga_name_text.get(), volume_number_text.get(), author_text.get()))

def update_command():
    database.update(selected_tuple[0], manga_name_text.get(), volume_number_text.get(), author_text.get())

def delete_command():
    database.delete(selected_tuple[0])

#Creating window
window = Tk()

window.wm_title("Manga Organizer") #name of window
window.configure(bg="#9F9F9F") #sets background color

#Labels
label1 = Label(window, text="Manga Name", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 10)) #fg is the text color
label1.grid(row=0, column=0)
label2 = Label(window, text="Volume Number", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 10))
label2.grid(row=0, column=2)
label3 = Label(window, text="Author", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 10))
label3.grid(row=1, column=2)
label4 = Label(window, text="Your Manga", bg="#9F9F9F", fg="#FFFFFF", font=("Arial", 15))
label4.grid(row=2, column=0, columnspan=2)

#Entries
manga_name_text = StringVar()
entry1 = Entry(window, textvariable=manga_name_text)
entry1.grid(row=0, column=1)
volume_number_text = StringVar()
entry2 = Entry(window, textvariable=volume_number_text)
entry2.grid(row=0, column=3)
author_text = StringVar()
entry3 = Entry(window, textvariable=author_text)
entry3.grid(row=1, column=3)

#List Box
list_box = Listbox(window, height=6, width=35)
list_box.grid(row=3, column=0, rowspan=6, columnspan=2)

#Scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=3, column=2, rowspan=6)

#Connecting Scrollbar and List Box
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

#Buttons
button1 = Button(window, text="View All Manga", width=15, bg="#404040", fg="#FFFFFF", command=view_command)
button1.grid(row=3, column=3)
button2 = Button(window, text="Search Volume", width=15, bg="#404040", fg="#FFFFFF", command=search_command)
button2.grid(row=4, column=3)
button3 = Button(window, text="Add New Volume", width=15, bg="#404040", fg="#FFFFFF", command=add_command)
button3.grid(row=5, column=3)
button4 = Button(window, text="Update Volume", width=15, bg="#404040", fg="#FFFFFF", command=update_command)
button4.grid(row=6, column=3)
button5 = Button(window, text="Delete Volume", width=15, bg="#404040", fg="#FFFFFF", command=delete_command)
button5.grid(row=7, column=3)

window.mainloop()

