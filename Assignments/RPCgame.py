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

def Playername():
    name = input()
    print(name)

Playername()

class Points:
    WinPoint = 2
    TiePoint = 1
    Loss = 0