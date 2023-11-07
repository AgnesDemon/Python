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

import json

data = json.load(open("data.json")) #opens the data.json file

#this function returns the data from the data.json file
def translate(w):
    return data[w]

word = input("Enter your word: ") #allows user to type in their word

print(translate(word)) #runs def translate and uses the user input in the word variable


