from tkinter import *
#import backend
from backend import Database #importing the class Database frm backend.py

database = Database() #OPTIONAL! PART 2: You can insert "books.db" into the parenthesis to name the .db file/window

def get_selected_row(event):
    global selected_tuple
    index = list.curselection()[0] #an index error will occur if you selected more than one #/letter with the cursor
    selected_tuple = list.get(index)
    #print(selected_tuple)
    #return(selected_tuple)
    entry1.delete(0, END) #makes sure entry1 is empty
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])

def view_command(): #allows us to see the books
    list.delete(0, END) #makes sure the listbox is empty
    for row in Database.view():
        list.insert(END, row)

def search_command(): #allows us to search for books by either their name, author, year, or isbn
    list.delete(0, END)
    for row in Database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list.insert(END, row)

def add_command(): #allows us to add more books
    Database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list.delete(0, END)
    list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command(): #deletes selected book
    Database.delete(selected_tuple[0])

def update_command(): #updates selected book
    Database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())    

window = Tk()

window.wm_title("Bookstore") #gives the window a name

button1 = Button(window, text="View All", width=12, command=view_command)
button1.grid(row=2, column=3)
button2 = Button(window, text="Search Entry", width=12, command=search_command)
button2.grid(row=3, column=3)
button3 = Button(window, text="Add Entry", width=12, command=add_command)
button3.grid(row=4, column=3)
button4 = Button(window, text="Update Selected", width=12, command=update_command)
button4.grid(row=5, column=3)
button5 = Button(window, text="Delete Selected", width=12, command=delete_command)
button5.grid(row=6, column=3)
button6 = Button(window, text="Close", width=12, command=window.destroy)
button6.grid(row=7, column=3)

title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)
author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)
year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)
isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

label1 = Label(window, text="Title")
label1.grid(row=0, column=0)
label2 = Label(window, text="Author")
label2.grid(row=0, column=2)
label3 = Label(window, text="Year")
label3.grid(row=1, column=0)
label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

list = Listbox(window, height=6, width=35)
list.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop()


#to make an executable file:
    #pip install pyinstaller
    #in the terminal, type pyinstaller frontend.py
    #this runs the called python file with pyinstaller
    #to run just one file and not any excess files, type pyinstaller --onefile frontend.py
    #if you want it to be windowed, add "--windowed" before frontend.py
    #NOTE: THIS CAUSED MY COMPUTER TO FREAK OUT ABOUT A VIRUS. I IMMEDIATELY DELETED THE FILE, BUT IF I HAVE TO MAKE A FILE LIKE THIS, LET DAD KNOW

#to access the Resouces file in files:
    #click on Downloads. The Resources file should be there
#to access my Visual Studio Code files:
    #click on This PC
    #double click on OS(C:)
    #double click on the Coding file
    #now I should have access to all my coding files