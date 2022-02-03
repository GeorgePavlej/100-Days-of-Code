from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wraper_function():
        return "<b>" + function() + "</b>"
    return wraper_function


def make_emphasis(function):
    def wraper_function():
        return "<em>" + function() + "</em>"
    return wraper_function


def make_underlined(function):
    def wraper_function():
        return "<u>" + function() + "</u>"
    return wraper_function


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name} you are {number} years old!"


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" \
           "<p>So this is  new paragraph!</p>" \
           "<img src='https://media.giphy.com/media/LukAHGCMfxMbK/giphy.gif' width=300>"


if __name__ == "__main__":
    app.run(debug=True)