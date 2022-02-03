from flask import Flask
import random


rand_number = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def home_route():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/JdFEeta1hLNnO/giphy.gif'>"


@app.route("/<int:number>")
def random_number(number):
    if number > rand_number:
        return "<h1 style='color:purple'>Too high, try again!</h1" \
               "<img src='https://media.giphy.com/media/27sdoZn8YhLbil01q6/giphy.gif'/>"

    elif number < rand_number:
        return "<h1 style='color:blue'>Too low, try again!</h1" \
               "<img src='https://media.giphy.com/media/ZrGQocLTUgIyrJcON2/giphy.gif'/>"
    else:
        return "<h1 style='color:red'>You found me!</h1" \
               "<img src='https://media.giphy.com/media/1kI8UsCjEwfiXc3TYy/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)