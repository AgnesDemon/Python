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


#NOTE: you should always create a virtual environment first before building an application
#need to pip install virtualenv
#this will allow me to create a virtual environment and not have excess libraries not needed for flask apps
#to create the virtual environment:
    #create a folder to hold the folder containing the app files (in this case, app_5)
    #in the terminal, type python -m venv virtual
    #a virtual folder should be created, and in that folder should be a few other folders with files
    #this will create the environment for us
    #next, type in virtual\Scripts\python in the terminal
    #this should open a python shell in the terminal
    #just exit it
    #you will need to install flask in your environment, so type virtual\Scripts\pip install flask
    #this should install flask
    #now, run the app by typing virtual\Scripts\python app_4\build_a_personal_website.py
    #it should be able to run
