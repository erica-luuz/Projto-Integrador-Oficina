from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators
from wtforms.fields.datetime import DateTimeField


class Addprodutos(Form):
    name = StringField('Nome :', [validators.DataRequired()])
    order_number = IntegerField('Numero Pedido :', [validators.DataRequired()])
    unitprice = IntegerField('Preço Unitário :', [validators.DataRequired()])
    total_price = IntegerField('Preço Total :', [validators.DataRequired()])
    quantity = IntegerField('Quantidade :', [validators.DataRequired()])
    colors = TextAreaField('Cor :', [validators.DataRequired()])
    size = StringField('Tamanho :', [validators.DataRequired()])
    description = TextAreaField('Descrição :', [validators.DataRequired()])


    image_1 = FileField('Image 1 :', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

