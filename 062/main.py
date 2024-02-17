from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)
load_dotenv()
app.config["SECRET_KEY"] = getenv("FLASK_SECRET_KEY_62")
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    opening_time = StringField("Opening Time e.g.8AM", validators=[DataRequired()])
    closing_time = StringField("Closing Time e.g.5:30PM", validators=[DataRequired()])
    cofee_rating = SelectField(
        "Cofee Rating",
        choices=[
            ("☕"),
            ("☕☕"),
            ("☕☕☕"),
            ("☕☕☕☕"),
            ("☕☕☕☕☕"),
        ],
    )
    wifi_rating = SelectField(
        "Wifi Strength Rating",
        choices=[
            ("✘"),
            ("💪"),
            ("💪💪"),
            ("💪💪💪"),
            ("💪💪💪💪"),
            ("💪💪💪💪💪"),
        ],
    )
    socket_available = SelectField(
        "Power Socket Availability",
        choices=[
            ("✘"),
            ("🔌"),
            ("🔌🔌"),
            ("🔌🔌🔌"),
            ("🔌🔌🔌🔌"),
            ("🔌🔌🔌🔌🔌"),
        ],
    )

    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")

        # form.data returns a dictionary so we are retrieving the values only from the dictionary
        for key, value in form.data.items():
            # ignoring the 'submit' and 'csrf_token' keys
            if key != "submit" and key != "csrf_token":
                # appending each value retrieved into the csv file separated by a comma
                with open(
                    "062/cafe-data.csv", "a", newline="", encoding="utf8"
                ) as csv_file:
                    # checks if it is the last entry then adds a new line and omits adding a comma if it is
                    if key == "socket_available":
                        csv_file.write(value + "\n")
                    else:
                        csv_file.write(value + ",")

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("062/cafe-data.csv", newline="", encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
