from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file("design.kv")

class LoginScreen(Screen):
    #pass
    def sign_up(self):
        #print("Sign up button is pressed")
        self.manager.current = "sign_up_screen"

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
        print(users)

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()