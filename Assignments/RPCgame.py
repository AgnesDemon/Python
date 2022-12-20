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
numberPlayers = 2

names = []

def playerName():
    print("Enter Player Name:")
    PlayerName = input()
    if (len(PlayerName) <= 0):
        print("No Manches! That's not a name. Please try again")
        playerName()
    else:
        names.append(PlayerName)
    
def numberOfPlayers():
    while len(names) < numberPlayers:
        playerName()
    print(names)

numberOfPlayers()

rps = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}

def randomGenerator():
    randomNumber = randint(1,3)
    print(rps[randomNumber])

def randomPlayerObjects():
    clear()
    for name in names:
        print(name)
        randomGenerator()

randomPlayerObjects()




