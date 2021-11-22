from wtforms import Form, BooleanField, StringField, PasswordField, form, validators

# Formulario de Registros de Usuarios
class RegistrationForm(Form):
    name = StringField('Nome completo :', [validators.Length(min=4, max=25)])
    username = StringField('Usuario :', [validators.Length(min=4, max=25)])
    email = StringField('Email :', [validators.Length(min=6, max=35)])
    password = PasswordField('Nova senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senha e confirmacao nao sao iguais')
    ])
    confirm = PasswordField('Repete a sua senha')

# Formulario de login 
class LoginFormulario(Form):
     email = StringField('Email :', [validators.Length(min=6, max=35)])
     password = PasswordField('senha', [validators.DataRequired()])
       