from flask import Flask, render_template, request
import pandas
import os
clear = lambda: os.system('cls')

app = Flask(__name__)

image_folder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')
def pageone():
    #img_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'img.png')
    with open('sampletext.txt', 'r') as file:
        filename = file.read()
    #return render_template("pageone.html", user_image = img_1, content=filename)
    return render_template("pageone.html", content=filename)

@app.route('/secondpage/')
def pagetwo():
    #img_2 = os.path.join(app.config['UPLOAD_FOLDER'], 'img2.png')
    #return render_template("pagetwo.html", user_image = img_2)
    with open('sampletext.txt', 'r') as file:
        #filename = file.read() #reads all text lines next to each other
        filename = file.readline() #reads only the first line of text file
    return render_template("pagetwo.html", content=filename)

if __name__ == "__main__":
    app.run(debug=True)
