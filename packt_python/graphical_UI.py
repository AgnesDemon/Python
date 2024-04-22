#you don't have to pip install tkinter because it is a built in python library
from tkinter import *

#Lesson window
#a tkinter program is made up of widgets and the window
'''window=Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

b1 = Button(window, text="Execute", command=km_to_miles) #designs the button (puts the word "Execute" on the button)
#b1.pack() #creates the button
b1.grid(row=0, column=0) #this method creates the button and places in a specific place
#to see the parameters for the Button() function, do this:
    #create a new terminal
    #type "ipython"
    #next, type "from tkinter import *" and press enter
    #now type "Button?"
    #this should show you all the parameters for Button()

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value) #creates an area where you can type (like a search bar)
e1.grid(row=0, column=1) #puts the search bar in a specific place

t1=Text(window, height=1, width=20) #this creates a text window
t1.grid(row=0, column=2)


window.mainloop()'''

#Assignment

window = Tk()

def kg_conversions():
    gram = float(entry_value.get())*1000
    text1.delete("1.0", END) #this clears the text box so that you can enter a new number
    text1.insert(END, gram)
    pound = float(entry_value.get())*2.20462
    text2.delete("1.0", END)
    text2.insert(END, pound)
    ounce = float(entry_value.get())*35.274
    text3.delete("1.0", END)
    text3.insert(END, ounce)

button = Button(window, text="Convert", command=kg_conversions)
button.grid(row=0, column=2)

entry_value=StringVar()
entry=Entry(window, textvariable=entry_value)
entry.grid(row=0, column=1)

label = Label(window, text="Kg") #this creates a label - you cannot interact with it
label.grid(row=0, column=0)

text1 = Text(window, height=1, width=20)
text1.grid(row=1, column=0)
text2 = Text(window, height=1, width=20)
text2.grid(row=1, column=1)
text3 = Text(window, height=1, width=20)
text3.grid(row=1, column=2)

window.mainloop()

#in this assignment, I am able to:
    #open a window with window and window.mainloop()
    #type in the entry bar with entry
    #click on the Convert button with button
    #convert kg into grams, pounds, and ounces with kg_conversions() and button
    #place the conversions in different text boxes using text1, text2, and text3
    #lets me type in new values without keeping the old ones
