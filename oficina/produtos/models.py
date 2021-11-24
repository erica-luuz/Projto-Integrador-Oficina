from oficina import db


class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True) # se for um nome que pode se repetir entao: unique=False
    name = db.Column(db.String(40), nullable=False, unique=True)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

db.create_all()
