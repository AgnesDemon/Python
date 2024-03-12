#Demo
#This is from the Justpy website tutorial on how to make a webpage
#Make sure when creating a webpage, there is a file in the same directory called "justpy.env"
#If there is no such file, the code will not work
#This demo creates a webpage, and in this webpage, there is a bar that says "Hello! Click me"
#If you click the bar, it will show how many times you have clicked on it in the bar itself, switching from the first phrase to "I've been clicked x times"
'''import justpy as jp

def hello_world():
    wp = jp.WebPage()
    jp.Hello(a=wp)
    return wp

jp.justpy(hello_world)'''


import justpy as jp

def app():
    webpage = jp.QuasarPage() #creates the webpage
    heading1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h1 text-center") #makes heading more modern, gives it a bigger font and centers it
    #to find fonts, styles, etc, search "quasar style" and click on the "Stylus Variables | Quasar Framework" webpage
    #this should show you different styles and identities that you can use for your webpage
    paragraph1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis") #creates a paragraph

    return webpage

jp.justpy(app) #calls app() function
#justpy() is a function that takes care of calling other functions
#when making updates to the code, you will have to stop it from running in the terminal by using Ctrl + C

