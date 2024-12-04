from flask import Flask, render_template, request
import pandas
import os

app = Flask(__name__)

image_folder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')
def pageone():
    img_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'img.png')
    return render_template("pageone.html", user_image = img_1)

@app.route('/secondpage/')
def pagetwo():
    #img_2 = os.path.join(app.config['UPLOAD_FOLDER'], 'img2.png')
    #return render_template("pagetwo.html", user_image = img_2)
    return render_template("pagetwo.html")

if __name__ == "__main__":
    app.run(debug=True)
