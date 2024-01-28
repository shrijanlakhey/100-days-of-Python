from flask import Flask

app = Flask(__name__)


# We can add variable sections to a URL by marking sections with <variable_name>
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, your roll number is {number}!"


if __name__ == "__main__":
    # setting 'debug=True' so that there is no need to keep on restarting the server manually and simply save the file to reflect the changes
    app.run(debug=True)
