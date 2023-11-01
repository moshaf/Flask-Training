from flask import Flask
import random


app = Flask(__name__)
number = random.randint(0,9)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9: </h1>"

@app.route("/<int:guess>")
def compare(guess):
    if guess > number:
        return "<h1 style='color:red'>Your Guess is too high!</h1>"
    elif number > guess:
        return "<h1 style='color:blue'>Your Guess is too low!<h1>"
    else:
        return "<h1 style='color:green'>Your are correct!<h1>"

@app.route("/<string:guess>")
def not_valid(guess):
    return f"<h1 style='color:red'>'{guess}' is not a number! please enter a number between 0 and 9<h1>"


if __name__ == "__main__":
    app.run(debug=True)
