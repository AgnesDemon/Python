from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #this will be the first webpage that you see
def home():
    return render_template("home.html") #this line accesses the home.html file, which has the text inside
    #return "Homepage" #this will be the text that shows up on the page

@app.route('/about/') #to access this webpage, go to the top with the link and add "/about/"
def about():
    return render_template("about.html") #accesses about.html file
    #return "About content" #this will be the text that shows up on this page

if __name__ == "__main__":
    app.run(debug=True)