from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

#spacing is internal; padding is external
#padding is the space between the cell edges and cell content
#spacing is the space between each cell
#sp means space-independent pixels
#size_hint makes widgets adjustable when you resize the screen
#when you set password: to True, it'll make the text in the textbox show stars, so that no one can see what you type
#text_size: self.width, None allows the text to be resizable, but if text is too large, text will overlap widgets
#setting height to a specific number in Label (ScrollView) will set the label itself to that specific height
#texture_size[1] has two items: the width of the text and the height.
#if it was [0] instead of [1], it would access the width instead of the height.

#USE LATER:
    #source: "logout_hover.png" if self.hovered else "logout_nothover.png"
    #NOTE: remove text: "Log out" from <LoginSuccessScreen> and replace with previous line beneath on_press

Builder.load_file("design.kv")

class LoginScreen(Screen):
    #pass
    def sign_up(self):
        #print("Sign up button is pressed")
        self.manager.current = "sign_up_screen"
    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
        if username in users and users[username]["password"] == password:
            self.manager.current = "login_success_screen"
        else:
           self.ids.wrong_login.text = "Wrong username or password"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    #pass
    def add_user(self, username, password):
        #pass
        #print(username, password)
        with open("users.json") as file:
            users = json.load(file)
        #print(users)
        users[username] = {"username": username, "password": password, 
                "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        #print(users)
        with open("users.json", "w") as file:
            json.dump(users, file)
        #NOTE: when making a json file, if you keep bumping into a JSONDecodeError, try putting curly brackets in the json file
        #NOTE: to switch into a more readable format in a json file, press Shift + Alt + F
        self.manager.current = "sign_up_success_screen"

class SignUpSuccessScreen(Screen):
    #pass
    def go_to_login(self):
        self.manager.transition.direction = "right" #makes the screen swipe to the right when switching
        self.manager.current = "login_screen"

class LoginSuccessScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    def get_quote(self, feeling):
        #print(feeling)
        feeling = feeling.lower()
        available_feelings = glob.glob("quotes/*txt")
        #print(available_feelings)
        available_feelings = [Path(filename).stem for filename in available_feelings]
        #print(available_feelings)
        if feeling in available_feelings:
            with open(f"quotes/{feeling}.txt", 'r', encoding="utf-8") as file: #without the "utf-8", I kept getting a charmap codec error
                quotes = file.readlines()
            #print(quotes)
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeing"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

#class HoverButton(Button, HoverBehavior):
    #pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()


#APK files are files that can be installed in Android phones as usable apps
#in order to create an APK file and store all files from app_7, I need to use the Buildozer library.
#Buildozer is a Python library that can easily be installed with pip
#it is a little tricky to make an APK file on Windows, but possible
#however, it is easier to do it with a Linux operating system, which I do not have
#NOTE: before doing anything, make sure I have kivy-buildozer-installer.sh saved in my app_7 folder
#I can install VirtualBox, which is a virtual computer, by going to virtualbox.org and clicking the download button

#INSTALLING KIVY, GIT AND BUILDOZER FOR ANDROID APP
    #install Git with "sudo apt install git"
    #install Buildozer with "git clone https://github.com/kivy/buildozer.git"
    #change directory to Buildozer with "cd buildozer/" (Idk if accurate at this time or not)
    #install setup.py with "sudo python3 setup.py install"
    #type "ls" to see what is included in a file
    #to make your project a Buildozer project, use "buildozer init"
    



    