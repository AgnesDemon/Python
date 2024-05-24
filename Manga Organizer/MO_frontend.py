#Should be able to log in
#Should be able to create folders for different manga series
#Should be able to add and store new manga into files
#Should organize manga in order by volume
#Volumes should include names, volume numbers, and authors
#Should be able to see the files
#Maybe delete files or manga
#Make sure I cannot make duplicates. This means that the manga can have the same name, but not the same volume number

from tkinter import *

window = Tk()

window.wm_title("Manga Organizer")

#Labels
label1 = Label(window, text="Manga Name")
label1.grid(row=0, column=0)
label2 = Label(window, text="Volume Number")
label2.grid(row=0, column=2)
label3 = Label(window, text="Author")
label3.grid(row=1, column=2)
label4 = Label(window, text="Your Manga")
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
#list_box.bind('<<ListboxSelect>>')

#Buttons
button1 = Button(window, text="View All Manga", width=15)
button1.grid(row=3, column=3)
button2 = Button(window, text="Search Volume", width=15)
button2.grid(row=4, column=3)
button3 = Button(window, text="Add New Volume", width=15)
button3.grid(row=5, column=3)
button4 = Button(window, text="Update Volume", width=15)
button4.grid(row=6, column=3)
button5 = Button(window, text="Delete Volume", width=15)
button5.grid(row=7, column=3)

window.mainloop()

