from flask import Flask
from random import randint

random_number = randint(0, 9)
print(random_number)
# guess = 0
app = Flask(__name__)


@app.route("/")
def home():
    return (
        "<h1>Guess the number between 0-9<h1>"
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    )


@app.route("/<int:guess>")
def guessed_num(guess):
    if random_number == guess:
        return (
            '<h1 style="color:green">You found me!</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3Vtdm94OTc5dXBhZTNieWw3OHU2cTJlN3Fzd2FnNjJnbmVjNnVlcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MWqc0k2qiD1As/giphy.gif" width=500>'
        )
    elif random_number > guess:
        return (
            '<h1 style="color:red">Too low, try again</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGcyam55czc4eXoxbWwwZGc0M2FycHQyZ2RicmNscWM3azZjNjF2NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4EoZ1rJtDfypcna8/giphy.gif" width=500>'
        )
    elif random_number < guess:
        return (
            '<h1 style="color:purple">Too high, try again</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWRtdHJwbXZyMHVsZmNtY2U3MmVyYWJmM2lpaGQ1ZmJmeHh1dHQ3MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4EpdXyNGauTcHovm/giphy.gif" width=500>'
        )


if __name__ == "__main__":
    app.run(debug=True)
