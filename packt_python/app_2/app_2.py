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
    #"get_close_matches("rainn", data.keys(), cutoff = 0.8)" gives you a list of similar words with the cutoff of 0.8, or percentage of similarity

import json
from difflib import get_close_matches

data = json.load(open("data.json")) #opens the data.json file

#this function returns the data from the data.json file
def translate(w):
    w = w.lower() #allows you to type capital letters and it won't cause an error
    if w in data:
        return data[w] #if word exists in the data.json file, return the definition
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y for yes or n for no: " % get_close_matches(w, data.keys())[0]) #get_close_matches() gives you the most similar word to what you typed
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word does not exist. Please double check it."
        else:
            return "We didn't understand your answer."
    else:
        #print("This word does not exist. Please double check it.") #prints phrase in terminal but also "None" underneath it
        return "The word doesn't exist. Please double check it." #prints phrase in terminal without "None" underneath it

word = input("Enter your word: ") #allows user to type in their word

output = translate(word) #assigns the function to a variable

if type(output) == list:
    for item in output:
        print(item) #if the output is a list, print the items in the list
else:
    print(output) #prints the output that isn't a list

