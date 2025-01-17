from flask import Flask, render_template, request
import os
import signal
clear = lambda: os.system('cls')

app = Flask(__name__)

inventory = 0
print(inventory)

inventory += 1
print(inventory)

lose_item = inventory - 1
print(lose_item)

@app.route("/", methods = ["GET", "POST"])
def start():
    text = {}
    index = 0
    with open("text_set_one.txt") as file:
        for line in file:
            index = index + 1
            text[index] = line.strip()
    if request.method == "POST":
        try:
            line_num = request.form.get('current_line')
            num = int(line_num) + 1
            return render_template("start.html", content = text[num], line_number = num)
        except:
            text = "Should you go on the trip? Type 'yes' or 'no' for your answer."
            return render_template("start.html", content = text)
    return render_template("start.html", content = text[1], line_number = 1)


'''def handle_shutdown():
    print("Shutting down Flask app")
    os._exit(0)

signal.signal(signal.SIGINT, handle_shutdown)'''

if __name__ == "__main__": #runs app
    app.run(debug=True)
