import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    # Select * from flights JOIN passengers ON flights.id = passengers.flight_id WHERE passengers.name = 'Alice';
    passenger = Passenger.query.filter_by(name='Alice').first().flight
    print(passenger)
    #print(f"{passenger.name}")

if __name__ == "__main__":
    with app.app_context():
        main()