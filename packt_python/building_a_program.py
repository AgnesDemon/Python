#my initial thought of how the input loop part of the program would work
'''while True:
    phrase = input("Say something: ")
    if phrase == "\end":
        break
    else:
        continue'''

def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    
#print(sentence_maker("how are you")) -- was used to test sentence_maker

results = [] #empty list
while True:
    user_input = input("Say something: ") #user types in input
    if user_input == "\end":
        break #function ends
    else:
        results.append(sentence_maker(user_input)) #sentence_maker funtion is called here
        #.append is adding user_input to the results list

print(" ".join(results)) #prints the list without the brackets
#"".join will join the strings without the brackets

