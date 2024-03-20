from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

# MovieDB
MOVIEDB_API_KEY = os.getenv("MOVIEDB_API_KEY")
MOVIEDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIEDB_DETAILS_URL = "https://api.themoviedb.org/3/movie/"
MOVIEDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# getting the absolute path of the current working directory
current_working_dir = os.getcwd()
subdir = "064"
# constructing the relative path for folder '063'
subdir_rel_path = os.path.join(current_working_dir, subdir)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{subdir_rel_path}/movies.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}"


with app.app_context():
    db.create_all()

    # Creating record
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
    # )
    # db.session.add(new_movie)
    # db.session.commit()


class EditMovieForm(FlaskForm):
    rating = FloatField(label="Your rating out of 10 e.g.7.5")
    review = StringField(label="Review")
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title")
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    """Display all movies"""
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    print(len(all_movies))
    for i in range(len(all_movies)):
        print(i)
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Search for the movie and return a list of movies with similar name"""
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        params = {
            "query": title,
            "api_key": MOVIEDB_API_KEY,
        }
        response = requests.get(url=MOVIEDB_SEARCH_URL, params=params)
        movie_detail = response.json()["results"]
        return render_template("select.html", movies=movie_detail)

    return render_template("add.html", form=form)


@app.route("/find", methods=["GET", "POST"])
def find_movie():
    """Find the detail of the selected movie and save it to the database"""
    movie_id = request.args.get("movie_id")
    if movie_id:
        moviedb_api_url = f"{MOVIEDB_DETAILS_URL}/{movie_id}"
        params = {"api_key": MOVIEDB_API_KEY, "language": "en-US"}
        response = requests.get(url=moviedb_api_url, params=params)
        movie_data = response.json()
        new_movie = Movie(
            title=movie_data["title"],
            img_url=f"{MOVIEDB_IMAGE_URL}{movie_data['poster_path']}",
            year=movie_data["release_date"].split("-")[0],
            description=movie_data["overview"],
        )
        db.session.add(new_movie)
        db.session.commit()
        new_movie_id = new_movie.id
        return redirect(url_for("edit", movie_id=new_movie_id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Edit movie's rating and review"""
    form = EditMovieForm()
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        new_rating = form.rating.data
        new_review = form.review.data

        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        return redirect(url_for("home"))
    movie_id = request.args.get("movie_id")
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    """Delete a movie's entry form the database"""
    movie_id = request.args.get("movie_id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
