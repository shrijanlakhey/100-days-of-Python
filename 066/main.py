from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from random import choice

"""
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

# getting the absolute path of the current working directory
current_working_dir = os.getcwd()
subdir = "066"
# constructing the relative path for folder '063'
subdir_rel_path = os.path.join(current_working_dir, subdir)


app = Flask(__name__)

# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{subdir_rel_path}/cafes.db"
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """returning a dictionary consisting the Cafe's data"""
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record


# HTTP DELETE - Delete Record


# since GET method is allowed by default, no need to specify GET method
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    # returns a list that includes all the cafes
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    cafes = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes=cafes)


@app.route("/search")
def get_cafe_at_location():
    location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes = result.scalars().all()
    if all_cafes:
        cafes = [cafe.to_dict() for cafe in all_cafes]
        return jsonify(cafes=cafes)
    else:
        # passing the HTTP code '404' along with the error response
        return (
            jsonify(error={"Not Found": f"Sorry, we don't have a cafe at {location}."}),
            404,
        )


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    cafe_to_update = db.session.execute(
        db.select(Cafe).where(Cafe.id == cafe_id)
    ).scalar()
    new_price = request.args.get("new_price")
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return (
            jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            ),
            404,
        )


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")

    if api_key == "TopSecretAPIKey":
        cafe_to_delete = db.session.execute(
            db.select(Cafe).where(Cafe.id == cafe_id)
        ).scalar()
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        else:
            return (
                jsonify(
                    error={
                        "Not Found": "Sorry a cafe with that id was not found in the database."
                    }
                ),
                404,
            )
    else:
        return (
            jsonify(
                error={
                    "Not Allowed": "Sorry, that's not allowed. Make sure you have the correct api_key"
                }
            ),
            403,
        )


if __name__ == "__main__":
    app.run(debug=True)
