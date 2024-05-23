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

label1 = Label(window, text="Manga Name")
label1.grid(row=0, column=0)
label2 = Label(window, text="Volume Number")
label2.grid(row=0, column=2)
label3 = Label(window, text="Author")
label3.grid(row=1, column=2)

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

