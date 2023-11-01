from flask import Flask

app = Flask(__name__)


# function passed around as argument
def add(n1, n2):
    return n1 + n2


def calc(func, n1, n2):
    return func(n1, n2)


result = calc(add, 3, 6)


@app.route("/")
def home():
    return f"<h1>This is the homepage {result}</h1>"


# create a simple decorator
def makeunderline(func):
    def wrapper():
        return "<u>" + func() + "</u>"

    return wrapper


@app.route("/index")
@makeunderline
def index():
    return f"<h1>This is the index page {result}</h1>"


# create an advanced decorator
def makeBold(func):
    def bolder(**kwargs):
        return "<b>" + func(kwargs["name"]) + "</b>"

    return bolder


@app.route("/bolder/<name>")
@makeBold
def make_bolder(name):
    return f"<p>This is the bolder page {name}</p>"


if __name__ == "__main__":
    app.run(debug=True)
