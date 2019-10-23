from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Persona(db.Model):
    __tablename__ = "personas"
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String, nullable=False)


class Cargo(db.Model):
    __tablename__ = "cargos"
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String, nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey("personas.id"), nullable=False)