#you don't have to pip install tkinter because it is a built in python library
from tkinter import *

#a tkinter program is made up of widgets and the window
window=Tk()

b1 = Button(window, text="Execute") #designs the button (puts the word "Execute" on the button)
#b1.pack() #creates the button
b1.grid(row=0, column=0) #this method creates the button and places in a specific place
#to see the parameters for the Button() function, do this:
    #create a new terminal
    #type "ipython"
    #next, type "from tkinter import *" and press enter
    #now type "Button?"
    #this should show you all the parameters for Button()

e1=Entry(window) #creates an area where you can type (like a search bar)
e1.grid(row=0, column=1) #puts the search bar in a specific place

t1=Text(window, height=5, width=20)
t1.grid(row=0, column=2)


window.mainloop()

