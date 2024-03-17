from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

# import sqlite3
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY_63")


#  normal way of creating database and adding entries (which is error prone!!!)
# db = sqlite3.connect("063/books-collection.db")
# cursor() allows Python code to execute PostgreSQL command in a database session
# cursor = db.cursor()

# creating table
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# adding data to the table
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# using SQLAlchemy (much better way)
# getting the absolute path of the current working directory
current_working_dir = os.getcwd()
subdir = "063"
# constructing the relative path for folder '063'
subdir_rel_path = os.path.join(current_working_dir, subdir)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{subdir_rel_path}/books-collection.db"
)
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()

    # CREATE RECORD
    # new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # db.session.add(new_book)
    # db.session.commit()

# with app.app_context():
# read all records
# all_books = db.session.query(Book).all()
# print(all_books)

# read a particular record by query
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)

# update a particular record by query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# update a record by primary key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# delete a particular book by primary key
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()


@app.route("/")
def home():
    # reading all the records
    all_books = db.session.query(Book).all()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Add a book"""
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }

        # creating record
        new_book = Book(
            title=new_book["title"],
            author=new_book["author"],
            rating=new_book["rating"],
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    """Edit a book's rating"""
    if request.method == "POST":
        book_id = request.form["id"]
        new_rating = request.form["rating"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("book_id")
    book = Book.query.get(book_id)
    print(book)
    return render_template("edit_rating.html", book=book)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    """Delete a book"""
    book_id = request.args.get("book_id")
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
