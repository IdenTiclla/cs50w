import os

from flask import Flask, render_template
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
    p = Persona(id=1, nombre_completo="Iden Ticlla Choque", telefono="77016596")
    db.session.add(p)
    db.session.commit()

    c = Cargo(id=1,descripcion="Jefe de Administracion")
    db.session.add(c)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        main()

 