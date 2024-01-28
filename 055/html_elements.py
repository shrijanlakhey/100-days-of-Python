from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    # here "\" is a ine continuation character. It breaks a long line of code into multiple lines for better readability without affecting the actual logic of the code.
    return '<h1 style = "text-align: center">Hello World!</h1>' \
            '<p>This is inside paragraph tag</p>'\
            '<img src="https://media.giphy.com/media/YWlH5gacq5CKRKWSRs/giphy.gif" width=300>'\


if __name__ == "__main__":
    app.run(debug=True)
