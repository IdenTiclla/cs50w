import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    # SELECT * FROM passengers WHERE flight_id = 1
    passengers = Flight.query.get(1).passengers
    for passenger in passengers:
        print(f"{passenger.name}")

if __name__ == "__main__":
    with app.app_context():
        main()