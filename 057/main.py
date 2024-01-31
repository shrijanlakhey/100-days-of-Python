from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/add2bddfa423b009d444"
posts = requests.get(blog_url).json()
post_objects = []
for post in posts:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_object)

print(post_objects[1].title)


@app.route("/")
def home():
    return render_template("index.html", posts=post_objects)


@app.route("/post/<int:post_id>")
def get_blog_details(post_id):
    """get the blog deetails of the selected id"""
    selected_post = None
    for post in post_objects:
        if post.id == post_id:
            selected_post = post
    return render_template("post.html", blog=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
