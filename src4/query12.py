import os

from flask import Flask, render_template, request
from models import *
from sqlalchemy import or_

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    """ SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id; """
    flights = db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
    for flight in flights:
        print(flight)

if __name__ == "__main__":
    with app.app_context():
        main()