import justpy as jp

'''def app():
    webpage = jp.QuasarPage() #creates the webpage
    heading1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h1 text-center") #makes heading more modern, gives it a bigger font and centers it
    #to find fonts, styles, etc, search "quasar style" and click on the "Stylus Variables | Quasar Framework" webpage
    #this should show you different styles and identities that you can use for your webpage
    paragraph1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis") #creates a paragraph

    return webpage

jp.justpy(app) #calls app() function
#justpy() is a function that takes care of calling other functions
#when making updates to the code, you will have to stop it from running in the terminal by using Ctrl + C'''

#Demo
import justpy as jp

def hello_world():
    wp = jp.WebPage()
    jp.Hello(a=wp)
    return wp

jp.justpy(hello_world)