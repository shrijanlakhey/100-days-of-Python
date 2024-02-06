from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
from os import getenv

load_dotenv()
MY_EMAIL = getenv("EMAIL")
MY_PASSWORD = getenv("PASSWORD")


app = Flask(__name__)

blog_url = "https://api.npoint.io/add2bddfa423b009d444"
# blog_url = "https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json"
all_posts = requests.get(blog_url).json()


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="lakheyshrijan@gmail.com",
                msg=f"Subject:New message\n\nName:{name} \nEmail:{email} \nPhone: {phone} \nMessage: {message}",
            )

        print(f"{name} \n{email} \n{phone} \n{message}")
        return render_template("contact.html", message_sent=True)
    else:
        return render_template("contact.html", message_sent=False)


@app.route("/post/<int:post_id>")
def get_blog_details(post_id):
    """get the blog deetails of the selected id"""
    selected_post = None
    for post in all_posts:
        if post["id"] == post_id:
            selected_post = post
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
