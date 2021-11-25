from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
from flask_bcrypt import Bcrypt
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minha oficina.db'
app.config['SECRET_KEY']='dsfgedbhef1234'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/image')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


from oficina.admin import rotas
from oficina.produtos import rotas

# Senha secreta, qualquer caracteres ex dsfgedbhef1234.