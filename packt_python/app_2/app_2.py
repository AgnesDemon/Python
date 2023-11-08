#BUILDING AN ENGLISH THESAURUS
#Program is designed to recieve a word (the input) and give its definition
#If a word is misspelled, the program should give a suggestion
#If the suggestion is the word you meant to type, then you can answer with Y/y/YES/yes/Yes
#If the suggestion is not the word you meant to type, then you can answer with N/n/NO/no/No
#If the word is too misspelled where the program cannot find a suggestion, it will give you a message saying that the word is not found

#data.json is classified as a dictionary
#in the python interactive shell, you can type 'data = json.load(open("data.json"))
#this will load the dictionary
#you can also type in a key from the dictionary in the python interactive shell, like this: 'data["rain"]'
#after executing this, you should get the definition
#make sure you are in the right directory
#dir(str) will show you the different string functions in the interactive python shell
#in interactive python shell:
    #"import difflib" imports difflib, which is a library used to compare text
    #"from difflib import SequenceMatcher" imports one of difflib's functions, SequenceMatcher
    #"SequenceMatcher(None, "rainn", "rain")" doesn't really do anything in particular
    #"SequenceMatcher(None, "rainn", "rain").ratio()" compares "rainn" and "rain" with a numerical value
    #"from difflib import get_close_matches" imports another difflib function
    #"get_close_matches("rainn", ["help", "pyramid", "rain"])" shows which word "rainn" compares most to
    #"get_close_matches("rainn", data.keys())" will give you a list of words similar to "rainn"
    #"get_close_matches("rainn", data.keys(), n = 5)" will give you more similar words in a list. In this case, 5 words
    #"get_close_matches("rainn", data.keys())[0]" gives you the first similar word in the list, or the closest matching word

import json

data = json.load(open("data.json")) #opens the data.json file

#this function returns the data from the data.json file
def translate(w):
    w = w.lower() #allows you to type capital letters and it won't cause an error
    if w in data:
        return data[w]
    else:
        #print("This word does not exist. Please double check it.") #prints phrase in terminal but also "None" underneath it
        return "The word doesn't exist. Please double check it." #prints phrase in terminal without "None" underneath it

word = input("Enter your word: ") #allows user to type in their word

print(translate(word)) #runs def translate and uses the user input in the word variable


