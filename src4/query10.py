import os

from flask import Flask, render_template, request
from models import *
from sqlalchemy import and_

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    """ SELECT * FROM flights WHERE origin = 'Paris' AND duration > 500 """
    flights = Flight.query.filter(and_(Flight.origin == "Paris", Flight.duration > 500)).all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()
