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
    
#print(sentence_maker("how are you")) was used to test sentence_maker

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input)) #sentence_maker funtion is called here

print(" ".join(results)) #prints the list without the brackets
#"".join will join the strings without the brackets

