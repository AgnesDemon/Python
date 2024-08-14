#open with a greeting
#*Could make the story present tense rather than past tense to keep players in suspense
#Endings I could have:
    #Beginning of the game - You could decline the invitation to go to Japan with your friends. Therefore, nothing really happens.
    #Optional marbles -You accept the invitation to Japan and go with your friends. While exploring, you meet a vendor who wants to sell you marbles. You can either decline or accept the marbles. Your choice will affect the story later.
    #You are in an area and want to get someplace. One friend suggests taking the short but eerie path. Another friend suggests taking the longer but seemingly safer path.
        #Shortcut: You take the eerie shortcut. Thankfully, nothing happens and you make it to your destination.
            #Shortcut ending: You take the shortcut and make it to your destination. However, while you are watching TV later, you find someone was murdered in the area of the long path. You realize that the victim could have been you or your friends.
        #Long path: You take the longer but safer path. There are more people around, and you bump into a strange woman wearing a large mask.
            #The woman asks you if you think she is pretty/beautiful/attractive. You are given three choices: Yes, No, and Average.
                #Average ending: You tell the woman she is average. She stares at you confused, then leaves.
                #No: You tell her she isn’t pretty. She will pull out bloody scissors and attempt to stab you.
                    #If you had bought the marbles, you can choose whether or not to throw them at her. If you don’t, you die. If you do, she will become distracted, giving you the time to run. This results in a trauma ending.
                #Yes: You tell the woman she is pretty. The woman seems to gleam under her mask. Slowly, she removes it, revealing something horrifying underneath. She will ask, “How about now?”.
                    #Scream: she will kill you unless you throw the marbles at her (if you have them). Endings: death or trauma.
                    #Yes: She will grin evilly and disfigure your face, just like hers, unless you throw the marbles at her (if you have them). Endings: disfigured face or trauma.
                        #Trauma ending explains how you go back home from Japan, feeling paranoid all the time and never wanting to venture out of the house.
                        #Disfigured ending explains how what the woman did left you scarred forever. You didn’t have enough money for a surgery, so you have to wear a mask for the rest of your life. Just like her.

import os
import time
clear = lambda: os.system("cls")

print("Welcome to my minigame!\nControls are simple: press Enter/Return to continue and type 'yes' or 'no' for answers.\nEnjoy!!")
time.sleep(7)
clear()

class Minigame():
    inventory = []

    def first_choice(this):
        choice1 = input("Your friends want to take a spontaneous trip to Japan. Do you want to go?\n")
        if choice1 == "no":
            clear()
            print("ENDING 1:\nYou decide not to go on the trip. Your friends are disappointed, but at least you survived.")
        elif choice1 == "yes":
            clear()
            #print("Congrats! You're going on a trip!") #need to change this to next phase
            this.second_choice()

    def second_choice(this):
        input("You decide to go on the trip. This is a once in a lifetime thing, so why not? Two days later, you boarded on a plane to Kyoto, Japan.")
        clear()
        input("Upon arrival, you take in the scenery before you: (insert scene here)") #need to do research on Nagasaki, Japan
        clear()
        input("However, despite your surroundings, you and your friends are exhausted, so you all take a taxi to your hotel and get some rest for the next day.")
        clear()
        input("The next day, you and your friends explore the city. Along the way, you meet a vendor, who is selling bags of marbles.")
        clear()
        choice2 = input("Do you want to buy the marbles?\n")
        if choice2 == "yes":
            for marbles in Minigame.inventory:
                Minigame.inventory.append(marbles) #list is showing up empty. Need to figure out why
            clear()
            input("You happily pay for the marbles.")
            print(Minigame.inventory)
        elif choice2 == "no":
            clear()
            input("You decide not to buy the marbles and walk away. You think that it would be best to save your money for a better souvenir.")
            print(Minigame.inventory)
        #this.third_choice()
    
    def third_choice(this):
        input()

    
    def run(this):
        this.first_choice()


minigame = Minigame()
minigame.run()