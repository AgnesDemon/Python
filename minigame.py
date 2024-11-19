#open with a greeting
#*Could make the story present tense rather than past tense to keep players in suspense
#Endings I could have:
    #Ending 1 - You could decline the invitation to go to Japan with your friends. Therefore, nothing really happens.
    #Optional marbles -You accept the invitation to Japan and go with your friends. While exploring, you meet a vendor who wants to sell you marbles. You can either decline or accept the marbles. Your choice will affect the story later.
    #You are in an area and want to get someplace. One friend suggests taking the short but eerie path. Another friend suggests taking the longer but seemingly safer path.
        #Shortcut: You take the eerie shortcut. Thankfully, nothing happens and you make it to your destination.
            #Ending 2: You take the shortcut and make it to your destination. However, while you are watching TV later, you find someone was murdered in the area of the long path. You realize that the victim could have been you or your friends.
        #Long path: You take the longer but safer path. There are more people around, and you bump into a strange woman wearing a large mask.
            #The woman asks you if you think she is pretty/beautiful/attractive. You are given three choices: Yes, No, and Average.
                #Ending 5: You tell the woman she is average. She stares at you confused, then leaves.
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

clear()
print("Welcome to my minigame!\nControls are simple: press Enter/Return to continue and type 'yes' or 'no' for answers.\nEnjoy!!")
time.sleep(2)
clear()

class Minigame():
    #inventory = []
    inventory = 0

    def first_choice(self):
        choice1 = input("Your friends want to take a spontaneous trip to Japan. Do you want to go?\n")
        if choice1 == "no":
            clear()
            print("ENDING 1:\nYou decide not to go on the trip. Your friends are disappointed, but at least you survived.")
        elif choice1 == "yes":
            clear()
            #print("Congrats! You're going on a trip!") #need to change this to next phase
            self.second_choice()
        else:
            clear()
            input("That is not a valid answer. Please try again.")
            clear()
            self.first_choice()

    def second_choice(self):
        input("You decide to go on the trip. This is a once in a lifetime thing, so why not? Two days later, you boarded on a plane to Kyoto, Japan.")
        clear()
        input("Upon arrival, you take in the scenery before you: (insert scene here)") #need to do research on Nagasaki, Japan
        clear()
        input("However, despite your surroundings, you and your friends are exhausted, so you all take a taxi to your hotel and get some rest for the next day.")
        clear()
        input("The following day arrives, and you and your friends explore the city. Along the way, you meet a vendor, who is selling bags of marbles.")
        clear()
        choice2 = input("Do you want to buy the marbles?\n")
        if choice2 == "yes":
            #for items in Minigame.inventory:
                #Minigame.inventory.append(items) #list is showing up empty. Need to figure out why
                #Minigame.inventory.append(items + 1) #error is occuring here
            #input(Minigame.inventory)
            #marbles = Minigame.inventory + 1
            Minigame.inventory += 1 #this works!!
            #input(marbles)
            clear()
            input("You happily pay for the marbles.")
            #input(Minigame.inventory)
            #return marbles - this makes the game stop running
        elif choice2 == "no":
            clear()
            input("You decide not to buy the marbles and walk away. You think that it would be best to save your money for a better souvenir.")
            #print(Minigame.inventory)
        self.third_choice()
    
    def third_choice(self):
        #input(Minigame.inventory) #inventory has already been emptied for some reason
        clear()
        input("After leaving the vendor, your friends get into an argument about where they should go next.")
        clear()
        input("Your first friend suggests that they should visit the temples. Cherry Blossoms are in season right now, so seeing the temples would be perfect timing.")
        clear()
        input("Your other friend suggests visting the Hashima Island. This is a once in a lifetime trip, and he figures that it would be best to see it first.")
        clear()
        choice3 = input("Should you visit the temples or the Hashima Island?\ntype 'temples' or 'island' as your answer\n")
        if choice3 == "temples":
            self.temples_route()
        elif choice3 == "island":
            self.island_route()
    
    def temples_route(self):
        clear()
        input("You agree with your first friend to visit the temples.")
        clear()
        input("After about an hour of walking and hiking, you make it to the temples. You snap photos of the temples and cherry blossoms with your cellphone.")
        clear()
        input("You and your friends spend some time at the temples taking pictures of everything before you all agree to get something to eat.")
        clear()
        input("After eating, you and your friends walk some more until the sun started setting. Then you headed back into the hotel to relax and rest your aching feet.")
        #input(Minigame.inventory)
        self.ending_2()
    
    def island_route(self):
        clear()
        input("You agree with your other friend to visit the Hashima Island.")
        clear()
        input("You book a ride on a boat to travel to the Hashima Island.")
        clear()
        input("Once you arrive, you get off the boat and explore the area with the other tourists and tourist guide.")
        clear()
        input("However, at some point in time, you get separated from your friends.")
        clear()
        input("You search for them everywhere, but can't seem to find them. While you weren't looking, you accidentally bump into a woman.")
        clear()
        input("'Oh! I'm sorry, ma'am!' You say quickly and bow your head.")
        clear()
        input("The lady looks at you, but you can't tell what her facial expression is because she is wearing a mask. She had long black hair and wore a pretty white dress.")
        clear()
        input("'Do you think I'm pretty?' She asks suddenly.")
        clear()
        input("'Pardon?' You ask, not sure if you heard her right.")
        clear()
        input("'Do you think I'm pretty?' She repeated.")
        self.fourth_choice()

    def ending_2(self):
        clear()
        if Minigame.inventory == 1:
            input("The rest of the trip goes off without a hitch. You have a bag of marbles as your souvenir and you got to see some beautiful sights.")
            clear()
            print("Ending 2: You enjoyed your trip.")
        elif Minigame.inventory == 0:
            input("The rest of the trip goes off without a hitch. You got a souvenir and you got to see some beautiful sights.")
            clear()
            print("Ending 2: You enjoyed your trip.")
            #keep getting this ending, even though I asked for the marbles
            #UPDATE: this ending keeps occuring because the inventory becomes empty at some point in the code
            #UPDATE2: fixed!! Now plays first ending when you ask for the marbles

    def fourth_choice(self):
        clear()
        choice4 = input("What should you say? Type 'yes', 'no', or 'so so' for your answer:\n")
        if choice4 == "yes":
            clear()
            input("'I think you're pretty, yeah.'")
            self.pretty_route()
        elif choice4 == 'so so':
            clear()
            input("It was difficult to tell because of the mask, but the woman seemed to be disappointed in your answer. She turned around and walked away, leaving you alone.")
        elif choice4 == "no":
            clear()
            input("It was difficult to tell because of the mask, but the woman seemed to be angry at your answer. From her pocket, she pulled out a pair of scissors that were stained with a suspicious red substance.")
    
    def pretty_route(self):
        clear()
        input("It was difficult to tell because of the mask, but she seemed to gleam at the complement. Slowly, she removed her mask. 'How about now?'")
        clear()
        input("You were horrified at the sight before you. The area around her mouth was disfigured with a long gash, giving her a horrifying grin.")
        clear()
        input("Slowly, she pulled out a pair of red stained scissors from her pocket, then started walking towards you. You freeze in fear.")
        if Minigame.inventory == 1:
            self.fifth_choice_a()
        elif Minigame.inventory == 0:
            self.fifth_choice_b()
    
    def fifth_choice_a(self):
        clear()
        input("What should do you? Suddenly you remember the marbles in your pocket.")
        clear()
        throw_marbles = input("Should you throw the marbles?\n")
        if throw_marbles == "yes":
            clear()
            Minigame.inventory - 1
            print(Minigame.inventory)
            input("You throw the marbles at her, distracting her. The you run as fast as you can away from the disfigured woman.")
            self.trauma_ending()
        elif throw_marbles == "no":
            self.death_ending()
    
    def fifth_choice_b(self):
        clear()
        input("You are too afraid to even move. You watch in horror as she gets closer to you.")
        clear()
        input("You hear a slash, and then everything goes black.")
        self.death_ending()

    
    def trauma_ending(self):
        clear()
        input("")
    
    def death_ending(self):
        clear()
        print("Ending 4: Your friends and family grieve your death.")

    def run(self):
        self.first_choice()


minigame = Minigame()
minigame.run()