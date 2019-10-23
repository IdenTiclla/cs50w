import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flight = Flight.query.filter_by(id=30).first()
    if flight:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")
    else:
        print(f"No se encontro vuelo con id: 1")
if __name__ == "__main__":
    with app.app_context():
        main()