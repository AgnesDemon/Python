from flask import Flask, render_template, request
import pandas
import os
import signal
clear = lambda: os.system('cls')

app = Flask(__name__) #creates app?

#image_folder = os.path.join('static','images')

#app.config['UPLOAD_FOLDER'] = image_folder

#1: turn file into dictionary, print out to make sure it works
#2: send first line number when there is no POST
#3: display number on html page
#4: put number in hidden input
#5: 

@app.route('/', methods=['GET', 'POST']) #creates page
def pageone():
    #img_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'img.png')
    with open('sampletext.txt', 'r') as file:
        filename = file.read() #reads all text lines next to each other
    #return render_template("pageone.html", user_image = img_1, content=filename)
    if request.method == "GET":
        return render_template("pageone.html", content=filename)
    input = request.form.get('input')
    if input == "yes":
        print("You typed 'yes'.")
    elif input == 'no':
        print("You typed 'no'.")
    else:
        print("Sorry, that is not a valid response.")
        return render_template("pageone.html", content=filename, text="Sorry, that is not a valid response.")
    #print(input)
    return render_template("pageone.html", content=filename)

@app.route('/secondpage/', methods=['GET', 'POST']) #creates page
def pagetwo():
    #img_2 = os.path.join(app.config['UPLOAD_FOLDER'], 'img2.png')
    #return render_template("pagetwo.html", user_image = img_2)
    text_dictionary = {}
    index = 0
    with open('sampletext.txt', 'r') as file:
        #linecount = len(file.readlines())
        #print(linecount)
        #line = file.readline() #reads only the first line of text file
        for line in file:
            index = index + 1
            text_dictionary[index] = line.strip()
    #print(text_dictionary)
    if request.method == "POST": #button has been pressed
        #print(request.form)
        try:
            line_num = request.form.get('current_line')
            num = int(line_num) + 1
        #print(line_num)
        #print("Button has been pressed")
        #while line:
            #line = line.strip()
            #line = file.readline() #can't do .readlines() because it will read all sentences at once
            return render_template("pagetwo.html", content= text_dictionary[num], line_number = num) #if this line isn't here, clicking submit will make text disappear
        except:
            #print("Out of text")
            text = "Do you want to read the lines again? Type 'yes' or 'no'."
            #return render_template("pageone.html", content = text) #can't put it here because then everything else doesn't work
            if request.method == "GET":
                return render_template("pageone.html", content = text)
            input = request.form.get('input')
            if input == "yes":
                #return render_template("pageone.html", content = text, text = "So you have chosen yes.")
                return render_template("pagetwo.html", content=text_dictionary[1], line_number = 1)
            elif input == 'no':
                #shutdown()
                handle_shutdown()
                #return render_template("pageone.html", content = text, text = "So you have chosen no.")
            #elif input == "":
                #return render_template("pageone.html", content = text) #This was pointless. Bottom message still appears
            else:
                return render_template("pageone.html", content = text, text = "Please type in a valid response.")
            #return render_template("pageone.html", content = text) #this won't work because of code before it
    return render_template("pagetwo.html", content=text_dictionary[1], line_number = 1) #this needs to be here, otherwise error will occur
    '''if request.method == "POST":
        with open('sampletext.txt', 'r') as file:
            print("Button has been pressed")
            line = file.readline()
            while line:
                line = line.strip()
                line = file.readline()
            return render_template("pagetwo.html", content=line)
    return render_template("pagetwo.html")'''
    '''with open('sampletext.txt', 'r') as file:
        line = file.readline()
        while line:
            if request.method == "POST":
                print("Button has been pressed")
                line = line.strip()
                line = file.readline()
                return render_template("pagetwo.html", content=line)
    return render_template("pagetwo.html", content=line)'''

'''@app.route('/shutdown', methods = ['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shutting down..."'''

def handle_shutdown():
    print("Shutting down Flask app")
    os._exit(0)

signal.signal(signal.SIGINT, handle_shutdown)

if __name__ == "__main__": #runs app
    app.run(debug=True)
