import os
clear = lambda: os.system('cls')


def login():
    print("Welcome to your local Manga Organizer! Please enter your username: ")
    username = input()
    clear()
    return username

print(login())