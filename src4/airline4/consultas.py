import os
from flask import Flask, render_template
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
    passenger = Passenger.query.filter_by(name="Hugo").first().flight
    print(passenger)

if __name__ == '__main__':
    with app.app_context():
        main()
 