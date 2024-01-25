from flask import Flask

app = Flask(__name__)
# '__name__' is a special attribute. It returns the name of the current class, method, function.
# 'print(__name__)' retruns '__main__' when run using command 'py.exe .\054\hello.py' meaning the code is run from a script or an interactive prompt but not form a module
# 'print(__name__)' returns 'hello' (name of the file) if the command 'flask --app 054/hello run' is used


# when a user navigates the site, this page loads up as home page as the page loads up after the slash (eg, http://127.0.0.1:5000/)
@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/bye")
def say_bye():
    return "<h1>Bye</h1>"


# now the program can run the Flask application using 'py.exe .\054\hello.py' command too
if __name__ == "__main__":
    app.run()
