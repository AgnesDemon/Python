from flask import Flask, render_template, request
import os
import signal
clear = lambda: os.system('cls')

class KuchisakeOnna:

    app = Flask(__name__)

    inventory = 0

#print(inventory)
#inventory += 1
#print(inventory)
#lose_item = inventory - 1
#print(lose_item)

    #need to create a main page for '/' so that it doesn't show the 'not found' page

    @app.route("/start", methods = ["GET", "POST"]) #need background, otherwise complete
    def start():
        #bedroom background
        text = {}
        index = 0
        with open("text_set_1.txt", 'r') as file:
            for line in file:
                index = index + 1
                text[index] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("start.html", content = text[num], line_number = num)
            except:
                text = "Should you go on the trip?"
                return render_template("first_choice.html", content = text)        
        return render_template("start.html", content = text[1], line_number = 1)

    @app.route("/firstending", methods = ["GET", "POST"]) #complete
    def firstending():
        #black background
        #should suggest to go back to the beginning to try again.
        fetext = {}
        feindex = 0
        with open("first_ending.txt", 'r') as file:
            for line in file:
                feindex = feindex + 1
                fetext[feindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("black_background.html", content = fetext[num], line_number = num)
            except:
                text = "Do you want to play again?"
                return render_template("back_to_beginning.html", content = text)
        return render_template("black_background.html", content = fetext[1], line_number = 1)

    @app.route("/secondpart", methods = ["GET", "POST"]) #needs background, otherwise complete
    def secondpart():
        #still working on what background I should put
        text2 = {}
        index2 = 0
        with open("text_set_2.txt", 'r') as file:
            for line in file:
                index2 = index2 + 1
                text2[index2] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = text2[num], line_number = num)
            except:
                candy_question = "Should you buy the candy?"
                #KuchisakeOnna.inventory += 1
                #print(inventory)
                return render_template("candy_choice.html", content = candy_question)
        return render_template("second_part.html", content = text2[1], line_number = 1)
    
    @app.route("/thirdpartcandy", methods = ["GET", "POST"]) #needs background, otherwise complete
    def thirdpartcandy():
        #vendors background
        text3 = {}
        index3 = 0
        with open("text_set_3.txt", 'r') as file:
            for line in file:
                index3 = index3 + 1
                text3[index3] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = text3[num], line_number = num)
            except:
                KuchisakeOnna.inventory += 1
                print(KuchisakeOnna.inventory)
                placechoice = "Which place should you go visit?"
                return render_template("place_choice.html", content = placechoice)
        return render_template("second_part.html", content = text3[1], line_number = 1)
    
    @app.route("/thirdpartnocandy", methods = ["GET", "POST"]) #needs background, otherwise complete
    def thirdpartnocandy():
        #vendors background
        text3 = {}
        index3 = 0
        with open("text_set_3.txt", 'r') as file:
            for line in file:
                index3 = index3 + 1
                text3[index3] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = text3[num], line_number = num)
            except:
                placechoice = "Which place should you go visit?"
                return render_template("place_choice.html", content = placechoice)
        return render_template("second_part.html", content = text3[1], line_number = 1)

    @app.route("/omurapark", methods = ["GET", "POST"]) #needs background, otherwise complete
    def omurapark():
        #omura park background
        print(KuchisakeOnna.inventory)
        optext = {}
        opindex = 0
        with open("omura_park.txt", 'r') as file:
            for line in file:
                opindex = opindex + 1
                optext[opindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = optext[num], line_number = num)
            except:
                if KuchisakeOnna.inventory == 1:
                    print("You have candy")
                    return render_template("good_ending_a.html")
                else:
                    print("You do not have candy")
                    return render_template("good_ending_b.html")
        return render_template("second_part.html", content = optext[1], line_number = 1)
    
    @app.route("/goodendinga", methods = ["GET", "POST"]) #complete
    def goodendinga():
        #black background
        #should suggest to go back to beginning or to go back to previous choice
        print(KuchisakeOnna.inventory)
        geatext = {}
        geaindex = 0
        with open("good_ending_a.txt", 'r') as file:
            for line in file:
                geaindex = geaindex + 1
                geatext[geaindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("black_background.html", content = geatext[num], line_number = num)
            except:
                back_question = "Would you like to play again?"
                return render_template("back_to_beginning.html", content = back_question)
        return render_template("black_background.html", content = geatext[1], line_number = 1)        

    @app.route("/goodendingb", methods = ["GET", "POST"]) #complete
    def goodendingb():
        #black background
        #should suggest to go back to beginning or to go back to previous choice
        print(KuchisakeOnna.inventory)
        gebtext = {}
        gebindex = 0
        with open("good_ending_b.txt", 'r') as file:
            for line in file:
                gebindex = gebindex + 1
                gebtext[gebindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("black_background.html", content = gebtext[num], line_number = num)
            except:
                back_question = "Would you like to play again?"
                return render_template("back_to_beginning.html", content = back_question)
        return render_template("black_background.html", content = gebtext[1], line_number = 1)

    @app.route("/hashimaisland", methods = ["GET", "POST"]) #needs background, otherwise complete
    def hashimaisland():
        #hashima island background, woman in background
        hitext = {}
        hiindex = 0
        with open("hashima_island.txt", 'r') as file:
            for line in file:
                hiindex = hiindex + 1
                hitext[hiindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = hitext[num], line_number = num)
            except:
                pretty_question = "What should you say? Is she pretty? Is she not pretty? Is she average?"
                return render_template("three_choice.html", content = pretty_question)
        return render_template("second_part.html", content = hitext[1], line_number = 1)

    @app.route("/pretty", methods = ["GET", "POST"]) #needs background, otherwise complete
    def pretty():
        #hashima island background with happy woman
        ptext = {}
        pindex = 0
        with open("pretty_1.txt", 'r') as file:
            for line in file:
                pindex = pindex + 1
                ptext[pindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = ptext[num], line_number = num)
            except:
                return render_template("pretty_2.html")
        return render_template("second_part.html", content = ptext[1], line_number = 1)

    @app.route("/pretty2", methods = ["GET", "POST"]) #needs background, otherwise complete
    def pretty2():
        #hashima island background, disfigured face woman
        print(KuchisakeOnna.inventory)
        p2text = {}
        p2index = 0
        with open("pretty_2.txt", 'r') as file:
            for line in file:
                p2index = p2index + 1
                p2text[p2index] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = p2text[num], line_number = num)
            except:
                if KuchisakeOnna.inventory == 1:
                    return render_template("candy.html")
                else:
                    return render_template("no_candy.html")
        return render_template("second_part.html", content = p2text[1], line_number = 1)

    @app.route("/candy", methods = ["GET", "POST"]) #needs background, otherwise complete
    def candy(): #this will be for pretty route to disfigured ending
        #hashima island background, disfigured face woman with scissors
        ctext = {}
        cindex = 0
        with open("candy.txt", 'r') as file:
            for line in file:
                cindex = cindex + 1
                ctext[cindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = ctext[num], line_number = num)
            except:
                candy_choice = "Should you throw the candy?"
                return render_template("throw_candy_choice.html", content = candy_choice)
        return render_template("second_part.html", content = ctext[1], line_number = 1)
    
    @app.route("/candy2", methods = ["GET", "POST"]) #needs background, otherwise complete
    def candy2(): #this will be for not pretty route to death ending
        #hashima island background, disfigured face woman with scissors
        ctext = {}
        cindex = 0
        with open("candy.txt", 'r') as file:
            for line in file:
                cindex = cindex + 1
                ctext[cindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = ctext[num], line_number = num)
            except:
                candy_choice = "Should you throw the candy?"
                return render_template("throw_candy_choice2.html", content = candy_choice)
        return render_template("second_part.html", content = ctext[1], line_number = 1)
    
    @app.route("/throwcandy", methods = ["GET", "POST"]) #needs background, otherwise complete
    def throwcandy():
        #hashima island background, candy thrown at woman
        tctext = {}
        tcindex = 0
        with open("throw_candy.txt", 'r') as file:
            for line in file:
                tcindex = tcindex + 1
                tctext[tcindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = tctext[num], line_number = num)
            except:
                return render_template("trauma_ending.html")
        return render_template("second_part.html", content = tctext[1], line_number = 1)

    @app.route("/dontthrowcandy", methods = ["GET", "POST"]) #completed
    def dontthrowcandy(): #leads to disfigured ending
        #bloody background
        dtctext = {}
        dtcindex = 0
        with open("dont_throw_candy.txt", 'r') as file:
            for line in file:
                dtcindex = dtcindex + 1
                dtctext[dtcindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                #return render_template("second_part.html", content = dtctext[num], line_number = num)
                return render_template("bloody_background.html", content = dtctext[num], line_number = num)
            except:
                return render_template("disfigured_ending.html")
        #return render_template("second_part.html", content = dtctext[1], line_number = 1)
        return render_template("bloody_background.html", content = dtctext[1], line_number = 1)
    
    @app.route("/dontthrowcandy2", methods = ["GET", "POST"]) #completed
    def dontthrowcandy2(): #leads to death ending
        #bloody background
        dtctext = {}
        dtcindex = 0
        with open("dont_throw_candy.txt", 'r') as file:
            for line in file:
                dtcindex = dtcindex + 1
                dtctext[dtcindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("bloody_background.html", content = dtctext[num], line_number = num)
            except:
                return render_template("death_ending.html")
        return render_template("bloody_background.html", content = dtctext[1], line_number = 1)

    @app.route("/nocandy", methods = ["GET", "POST"]) #completed
    def nocandy(): #pretty route, disfigured ending
        #bloody background
        nctext = {}
        ncindex = 0
        with open("no_candy.txt", 'r') as file:
            for line in file:
                ncindex = ncindex + 1
                nctext[ncindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("bloody_background.html", content = nctext[num], line_number = num)
            except:
                return render_template("disfigured_ending.html")
        return render_template("bloody_background.html", content = nctext[1], line_number = 1)
    
    @app.route("/nocandy2", methods = ["GET", "POST"]) #completed
    def nocandy2(): #not pretty route, death ending
        #bloody background
        nctext = {}
        ncindex = 0
        with open("no_candy.txt", 'r') as file:
            for line in file:
                ncindex = ncindex + 1
                nctext[ncindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("bloody_background.html", content = nctext[num], line_number = num)
            except:
                return render_template("death_ending.html")
        return render_template("bloody_background.html", content = nctext[1], line_number = 1)

    @app.route("/soso", methods = ["GET", "POST"]) #needs background, otherwise complete
    def soso():
        #hashima island background, disappointed woman
        sstext = {}
        ssindex = 0
        with open("so_so.txt", 'r') as file:
            for line in file:
                ssindex = ssindex + 1
                sstext[ssindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = sstext[num], line_number = num)
            except:
                return render_template("neutral_ending.html")
        return render_template("second_part.html", content = sstext[1], line_number = 1)

    @app.route("/neutralending", methods = ["GET", "POST"]) #complete
    def neutralending():
        #black background
        netext = {}
        neindex = 0
        with open("neutral_ending.txt", 'r') as file:
            for line in file:
                neindex = neindex + 1
                netext[neindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("black_background.html", content = netext[num], line_number = num)
            except:
                replay = "Would you like to play again?"
                return render_template("back_to_beginning.html", content = replay)
        return render_template("black_background.html", content = netext[1], line_number = 1)

    @app.route("/notpretty", methods = ["GET", "POST"]) #needs background, otherwise complete
    def notpretty():
        #hashima island background, angry woman with scissors
        nptext = {}
        npindex = 0
        with open("not_pretty.txt", 'r') as file:
            for line in file:
                npindex = npindex + 1
                nptext[npindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("second_part.html", content = nptext[num], line_number = num)
            except:
                if KuchisakeOnna.inventory == 1:
                    return render_template("candy2.html")
                else:
                    return render_template("no_candy2.html")
        return render_template("second_part.html", content = nptext[1], line_number = 1)

    @app.route("/traumaending", methods = ["GET", "POST"]) #complete
    def traumaending():
        #black background
        #should suggest going back to beginning or to previous choice
        tetext = {}
        teindex = 0
        with open("trauma_ending.txt", 'r') as file:
            for line in file:
                teindex = teindex + 1
                tetext[teindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("black_background.html", content = tetext[num], line_number = num)
            except:
                replay = "Would you like to play again?"
                return render_template("back_to_beginning.html", content = replay)
        return render_template("black_background.html", content = tetext[1], line_number = 1)

    @app.route("/disfiguredending", methods = ["GET", "POST"]) #complete
    def disfiguredending():
        #black background
        detext = {}
        deindex = 0
        with open("disfigured_ending.txt", 'r') as file:
            for line in file:
                deindex = deindex + 1
                detext[deindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("black_background.html", content = detext[num], line_number = num)
            except:
                replay = "Would you like to play again?"
                return render_template("back_to_beginning.html", content = replay)
        return render_template("black_background.html", content = detext[1], line_number = 1)
    
    @app.route("/deathending", methods = ["GET", "POST"]) #complete
    def deathending():
        #black background
        deathtext = {}
        deathindex = 0
        with open("death_ending.txt", 'r') as file:
            for line in file:
                deathindex = deathindex + 1
                deathtext[deathindex] = line.strip()
        if request.method == "POST":
            try:
                line_num = request.form.get('current_line')
                num = int(line_num) + 1
                return render_template("black_background.html", content = deathtext[num], line_number = num)
            except:
                replay = "Would you like to play again?"
                return render_template("back_to_beginning.html", content = replay)
        return render_template("black_background.html", content = deathtext[1], line_number = 1)


    '''def handle_shutdown():
        print("Shutting down Flask app")
        os._exit(0)

    signal.signal(signal.SIGINT, handle_shutdown)'''

if __name__ == "__main__": #runs app
    KuchisakeOnna.app.run(debug=True)



'''if request.method == "GET":
                    return render_template("question_page.html", content = text)
                input = request.form.get('input')
                if input == "yes":
                    file.close()
                    KuchisakeOnna.secondpart()
                    return render_template("second_part.html", content = KuchisakeOnna.secondpart.text2[1], line_number = 1)
                elif input == "no":
                    ending_line = "You decide that it's not the best idea. Your friends are disappointed, but they understand. \nEnding: You don't go on the trip."
                    return render_template("start.html", content = ending_line)
                else:
                    return render_template("question_page.html", content = text, text = "Please type in a valid response.")'''