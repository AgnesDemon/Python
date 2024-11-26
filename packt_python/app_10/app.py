from flask import Flask, render_template, request, send_file
import pandas
from geopy.geocoders import Nominatim

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
    if request.method == "POST":
        file = request.files["file"]
        try:
            dataframe = pandas.read_csv(file)
            #gc = Nominatim()
            #dataframe["coordinates"] = dataframe['Address'].apply(gc.geocode)
            #dataframe['Latitude'] = dataframe['coordinates'].apply(lambda x: x.latitude if x != None else None)
            #dataframe['Longitude'] = dataframe['coordinates'].apply(lambda x: x.longitude if x != None else None)
            #dataframe = dataframe.drop('coordinates',1)
            dataframe.to_csv("CSV_files/test_file.csv", index=None)
            return render_template("geocoder.html", text=dataframe.to_html(), btn="download.html")
        except:
            return render_template("geocoder.html", text="Please make sure you have an Address column in your .csv file")

@app.route("/download_file/")
def download():
    return send_file("CSV_files/test_file.csv", attachment_filename="yourfile.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)




