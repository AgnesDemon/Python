from flask import Flask, render_template, request
import pandas
import os

app = Flask(__name__)

image_folder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')
def pageone():
    img_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'sample_image1.png')
    return render_template("pageone.html", user_image = img_1)

if __name__ == "__main__":
    app.run(debug=True)
