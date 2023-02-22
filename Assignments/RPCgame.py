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
    id = 0
    name = None
    score = 0

    def __init__(this, player_name, id):
        this.name = player_name
        this.id = id
    








'''


#rps_generator()


    

    return winner'''



#player_objects()


    

class Game:
    number_players = 2
    players: list [Player] = []
    rps = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}
    rounds = 3
    round = []

    def get_players(this):
        while len(this.players) < this.number_players:
            player_id = len(this.players) +1
            name = Game.get_player_name()
            player = Player(name, player_id)
            this.players.append(player)

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

    def rps_generator(this):
        random_object = randint(1,3)
        #print(rps[random_object])
        return this.rps[random_object]


    def run_round(this):
        round_data= {}
        for player in this.players:
            name = player.name
            object = this.rps_generator()
            round_data[player.id] = object
            print(name, object)
        this.get_winner(round_data)
        input("Press Enter for the next round...")
        return round_data
    
    def get_winner(this, round_data):
        player_1_object = round_data[1]
        player_2_object = round_data[2]
        if player_1_object == "Rock":
            if player_2_object == "Scissors":
                return 1
            if player_2_object == "Paper":
                return 2
        if player_1_object == "Scissors":
            if player_2_object == "Paper":
                return 1
            if player_2_object =="Rock":
                return 2
        if player_1_object == "Paper":
            if player_2_object == "Rock":
                return 1
            if player_2_object == "Scissors":
                return 2






    def game_rounds(this):
        while len(this.round) < this.rounds:
            rnd = this.run_round()
            this.round.append(rnd)
        else:
            exit()
    
    def run(this):
        #get players
        this.get_players()

        #run a round
        this.game_rounds()
        #display results


game = Game()
game.run()














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

















