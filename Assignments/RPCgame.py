#Rock, paper, scissors:
#Collect player names
#Save Players' score (3/5/7) - win: 2 points, Tie: 1 point for each player, loss: 0 points per round
#Score is the sum of all won rounds / player
#Gotchas: what to do with ties
#Use classes whenever possible
#Make sure output is clean
#Use loops

#Rules of the game:
    #Rock beats scissors
    #Scissors beats paper
    #Paper beats rock

#I can use a while loop for whenever the person wants to play again
#I can use a class for the points
#Need to figure out a way to add Players' points
import os
clear = lambda: os.system('cls')
from random import randint

clear()
#Players

class Player:
    name = None
    score = 0

    def __init__(this, player_one):
        this.name = player_one
    
    def get_player_names():
        name = input("Enter Player 1 Name: ")
        if (len(name) <= 0):
            print("Sorry, that is not a valid name.")
            Player.get_player_names()

    get_player_names()



#number_players = 2

#names = []

'''def player_name():
    print("Enter Player Name:")
    Player_Name = input()
    if (len(Player_Name) <= 0):
        print("No Manches! That's not a name. Please try again")
        player_name()
    else:
        names.append(Player_Name)
    
def number_of_players():
    while len(names) < number_players:
        player_name()
    print(names)

number_of_players()

rps = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}

def random_generator():
    random_number = randint(1,3)
    print(rps[random_number])

def random_player_objects():
    clear()
    for name in names:
        print(name)
        random_generator()

random_player_objects()'''





