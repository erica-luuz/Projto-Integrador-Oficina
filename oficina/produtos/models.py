from oficina import db

from datetime import datetime



class Addproduto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    order_number = db.Column(db.Numeric(10), nullable=False)
    unitprice = db.Column(db.Numeric(10,2), nullable=False)
    total_price = db.Column(db.Numeric(10,2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    size = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'),nullable=False)
    fornecedor = db.relationship('Fornecedor', backref=db.backref('fornecedores', lazy=True))

    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'),nullable=False)
    categoria = db.relationship('Categoria', backref=db.backref('categorias', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image.jpg')


    def __repr__(self):
        return '<Addproduto %r>' % self.name





class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True) # se for um nome que pode se repetir entao: unique=False
    name = db.Column(db.String(40), nullable=False, unique=True)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

db.create_all()
