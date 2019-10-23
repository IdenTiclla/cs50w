import os

from flask import Flask, render_template
from models import * 
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
    print("TODOS LOS CARGOS..")
    # select * from cargos
    cargos = Cargo.query.all()
    for cargo in cargos:
        print(f"{cargo.id} {cargo.descripcion}")


    print("CARGO CON id = 1")
    # select * from cargos where id = 1
    cargo = Cargo.query.get(1)
    print(f"{cargo.id}, {cargo.descripcion}")


    print("CARGO CON id = 2")
    # select * from cargos where id = 2
    cargo = Cargo.query.filter_by(id=2).first()
    print(f"{cargo.id}, {cargo.descripcion}")

    # select count(*) from cargos
    amount = Cargo.query.count()
    print(f"la cantidad de tuplas en la tabla cargos es: {amount}")

    # select count(*) from personas
    amount = Persona.query.count()
    print(f"la cantidad de tuplas en la tabla personas es: {amount}")

    # Select * from personas
    personas = Persona.query.all()
    for persona in personas:
        print(f"{persona.id}, {persona.nombre_completo}, {persona.telefono}")

    # update personas set telefono = '69091721' where id = 1

    persona = Persona.query.get(1)
    persona.telefono = "69091721"
    print(f"{persona.id}, {persona.nombre_completo}, {persona.telefono}")
    #db.session.add(persona)
    db.session.commit()

    # PERSONAS QUE TIENEN UNA a en su nombre
    print("PERSONAS QUE TIENEN UNA a en su nombre")
    personas = Persona.query.filter(Persona.nombre_completo.like("%a%")).all()
    print(personas)
    for persona in personas:
        print(f"{persona.id}, {persona.nombre_completo}, {persona.telefono}")


    # DELETE
    #persona = Persona.query.get(3)
    #db.session.delete(persona)
    #db.session.commit()
if __name__ == '__main__':
    with app.app_context():
        main()
 