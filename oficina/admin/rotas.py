from flask import render_template, session, request, redirect, url_for, flash

from oficina import app, db, bcrypt
from .forms import RegistrationForm, LoginFormulario 
from .models import User
import os



# rota da Home Pagina Administrativa
@app.route('/')
def home():
    return render_template ('admin/index.html', title='Página Administrativa')


# rota do cadastro de usuario
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():

        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit   #adicionado para salvar no bd
        flash(f'Obrigado {form.name.data} por registrar', 'success')

        return redirect(url_for('home'))
    return render_template('admin/Registrar.html', form=form, title="Registrar Usuários")

    # Rota do Formulario de Login
@app.route('/login',methods=['Get','POST'])
def login():
    form=LoginFormulario(request.form)
    return render_template ('admin/Login.html', form=form, title='Página Login')
   