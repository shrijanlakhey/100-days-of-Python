from flask import Flask

app = Flask(__name__)


def make_bold(function):
    """makes text bold"""
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    """makes text italic"""
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function

def make_underlined(function):
    """underlines the text"""
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
