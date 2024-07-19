from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random

#spacing is internal; padding is external
#sp means space-independent pixels
#size_hint makes widgets adjustable when you resize the screen

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

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()



    