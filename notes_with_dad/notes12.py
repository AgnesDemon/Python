#Hangman requirements:
#1. Someone or computer needs to guess a word (probably best to let 
# someone type in a phrase to solve)
#2. Draw a blank line for each leter in the word.
    #Example: Happy Birthday --> ----- --------
#3. While loop that allows player to guess until they win 
# or the man is dead
#4. Display the used letters
#5. Fill in correct letters (all instances of the letters)
#6. Drawing the man:
    #a. Draw the post
    #b. Draw the head
    #c. Draw the body (single line)
#7. Allow user to guess once, counts as a bad letter if they get it wrong.


#Set up some game instructions
#Draw instructions
import getpass
import hangman_art
import os
clear = lambda: os.system('cls')

class Hangman:
    word = None
    used_letters = None
    wrong_choices = None
    word_guesses = None
    in_progress = False

    def __init__(this, word):
        this.word = word
        this.used_letters = []
        this.wrong_choices = 0
        this.word_guesses = 0
        this.in_progress = True
    
    def start(this):
        while this.in_progress:
            this.__draw_ui()
    
    def __draw_ui(this):
        clear()
        #draws the current hangman board
        this.__determine_winner()
        print(hangman_art.HANGMANPICS[this.wrong_choices])
        print()
        this.__draw_secret_word()
        print()
        patterned_word = this.__draw_used_letters()
        print(patterned_word)
        print()
        print()
        this.__get_next_letter()
    
    def __determine_winner(this, patterned_word):
        if '-' not in patterned_word:
            clear()
            print(hangman_art.VICTORY)
            exit()
        if this.wrong_choices >= 7:
            clear()
            print(hangman_art.GAME_OVER)
            exit()        
    
    def __get_next_letter(this):
        print("Please choose a letter:")
        letter = input()
        # Perform validation to make sure that they typed 1 character
        this.used_letters.append(letter)
        if letter not in this.word:
            this.wrong_choices += 1


    def __draw_used_letters(this):
        print("Used letters:")
        print(this.used_letters)

    def __draw_secret_word(this):
        patterned_word = ''
        # how should we handle spaces in the word?
        for char in this.word:
            if char in this.used_letters:
                patterned_word += char
            elif char == ' ':
                patterned_word += ' '
            else:
                patterned_word += '-'
        return patterned_word
    
# Use this to collect the starting phrase, ensuring that its spelled correctly
def get_game_phrase():
    valid_phrase = ''
    while len(valid_phrase) <= 0:
        phrase = getpass.getpass("Please proved a word to get started:\n")
        verify = getpass.getpass("Please verify your word or phrase:\n")
        if phrase == verify:
            valid_phrase = verify
        else:
            print("The word or phrase did not match...")
    return valid_phrase

clear()
game_phrase = get_game_phrase()
#getpass in this case allows input typed in to be invisible while person is typing
game = Hangman(game_phrase)
print(game.word)

for art in hangman_art.HANGMANPICS:
    print(art)
#print(hangman_art.HANGMANPICS)

#

