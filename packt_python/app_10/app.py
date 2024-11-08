from flask import Flask, render_template, request, send_file
import pandas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/geocoder/")
def geocoder():
    #csv_file = pandas.read_csv("test_file.csv")
    return render_template("geocoder.html")
    #return csv_file.to_html()

@app.route("/success_table", methods=["POST"])
def success_table():
    return render_template

if __name__ == "__main__":
    app.run(debug=True)