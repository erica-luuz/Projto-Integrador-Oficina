from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators


class Addprodutos(Form):
    name = StringField('Nome : '[validators.DataRequired()])
    order_number = IntegerField('Num Pedido : '[validators.DataRequired()])
    unitprice = IntegerField('Preço Unitário :'[validators.DataRequired()])
    total_price = IntegerField('Preço Total :'[validators.DataRequired()])
    date_entry = IntegerField('Data Entrada :'[validators.DataRequired()])
    date_out = IntegerField('Data Saída :'[validators.DataRequired()])
    Quantity = IntegerField('Quantidade :'[validators.DataRequired()])
    description = TextAreaField('Descrição :'[validators.DataRequired()])
    colors = TextAreaField('Cor :'[validators.DataRequired()])
    size = StringField('Tamanho :'[validators.DataRequired()])

    image_1 = FileField('Imagem 1 :', validators=[FileRequired(), FileAllowed(['jpg', 'pmg', 'gif', 'jpeg'])
    image_2 = FileField('Imagem 2 :', validators=[FileRequired(), FileAllowed(['jpg', 'pmg', 'gif', 'jpeg'])
