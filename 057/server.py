from flask import Flask, render_template
from random import randint
import datetime
import requests

app = Flask(__name__)


@app.route("/jinjabasics")
def jinja_basics():
    random_number = randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("jinjabasics.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    """uses API to guess the user's name and age"""
    params = {
        "name": name.capitalize(),
    }
    agify = requests.get("https://api.agify.io", params=params)
    age_data = agify.json()
    age = age_data["age"]

    genderize = requests.get("https://api.genderize.io", params=params)
    gender_data = genderize.json()
    gender = gender_data["gender"]

    return render_template("guess.html", age=age, gender=gender, user_name=name)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/add2bddfa423b009d444"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
