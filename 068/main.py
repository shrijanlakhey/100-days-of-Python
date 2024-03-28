from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

# getting the absolute path of the current working directory
current_working_dir = os.getcwd()
subdir = "068"
# constructing the relative path for folder '068'
subdir_rel_path = os.path.join(current_working_dir, subdir)


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{subdir_rel_path}/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# for dealing with login
login_manager = LoginManager()
login_manager.init_app(app)
# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = {
            "name": request.form["name"],
            "email": request.form["email"],
            "password": request.form["password"],
        }
        user = User.query.filter_by(email=new_user["email"]).first()
        # checks if the user with the entered email does not exist
        if not user:
            new_user = User(
                name=new_user["name"],
                email=new_user["email"],
                # hashing user's password using 'pbkdf2:sha256'
                password=generate_password_hash(
                    password=new_user["password"],
                    method="pbkdf2:sha256",
                    salt_length=8
                )
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect("secrets")
        else:
            flash("You've already signed up with that email, log in insread!")
            return redirect(url_for("register"))
    return render_template("register.html")


@ app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_credentials = {
            "email": request.form["email"],
            "password": request.form["password"],
        }
        # searching the user in database through user's email
        user = User.query.filter_by(email=login_credentials["email"]).first()
        # checking if the passwords match
        if user:
            if check_password_hash(pwhash=user.password, password=login_credentials["password"]):
                print("Password correct")
                # authenticating the user
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Password incorrect, please try again.")
                return redirect(url_for("login"))
        else:
            flash("That email does not exist, please try again.")
            return redirect(url_for("login"))
    return render_template("login.html")


@ app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@ app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@ app.route('/download/<path:name>')
@login_required
def download(name):
    return send_from_directory('static', name)


if __name__ == "__main__":
    app.run(debug=True)
