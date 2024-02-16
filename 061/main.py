from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from dotenv import load_dotenv
from os import getenv
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

load_dotenv()
app.secret_key = getenv("FLASK_SECRET_KEY_61")


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[validators.DataRequired(), validators.Email()],
    )
    password = PasswordField(
        label="Password",
        validators=[validators.DataRequired(), validators.Length(min=8)],
    )
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        form_email = form.email.data
        form_password = form.password.data

        if form_email == "admin@email.com" and form_password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


@app.route("/wtf_form")
def wtf_form():
    form = LoginForm()
    return render_template("wtf_form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
