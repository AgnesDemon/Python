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

#Players

class Player:
    name = None
    score = 0

    def __init__(this, player_name):
        this.name = player_name
    
    def get_player_name():
        clear()
        name = ""
        while (len(name) <= 0):
            clear()
            name = input("Enter Player Name: ")
            if len(name) > 0:
                clear()
                input("Welcome! Press enter to continue...")
                return name
            else:
                clear()
                input("Sorry, that is not a valid name.")

number_players = 2
players: list [Player] = []

def get_players():
    while len(players) < number_players:
        name = Player.get_player_name()
        player = Player(name)
        players.append(player)

get_players()

rps = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}

def rps_generator():
    random_object = randint(1,3)
    #print(rps[random_object])
    return rps[random_object]

#rps_generator()

def get_winner(round_data):
    print(round_data)
    

    return winner

def run_round():
    round_data = {}
    for player in players:
        name = player.name
        object = rps_generator()
        round_data[name] = object
        print(name, object)
    get_winner(round_data)
    input("Press Enter for the next round...")

#player_objects()

rounds = 3
round = []

def game_rounds():
    while len(round) < rounds:
        rnd = run_round()
        round.append(rnd)
    else:
        exit()

game_rounds()
    
















    #for round in rounds:
        #round = player_objects()
    #while round < 3:
#Didn't finish it, but sure that it won't work.

    #for round in rounds:
        #return round
    #while round < 3:
        #player_objects()
#Could only run first round, but had trouble running second one

    #while len(round) < rounds:
        #player_objects()
    #else:
        #exit()
#Keeps going infinitely, but works

    #for round in rounds:
        #return round
    #while round < rounds:
        #player_objects()
#Couldn't even run one round

















