from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaoficina.db'
app.config['SECRET_KEY']='dsfgedbhef1234'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from oficina.admin import rotas
from oficina.produtos import rotas

# Senha secreta, qualquer caracteres ex dsfgedbhef1234.