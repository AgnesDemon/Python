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

def handle_shutdown():
    print("Shutting down Flask app")
    os._exit(0)

signal.signal(signal.SIGINT, handle_shutdown)

if __name__ == "__main__": #runs app
    app.run(debug=True)
