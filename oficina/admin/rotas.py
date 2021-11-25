from flask import render_template, session, request, redirect, url_for, flash
from oficina.produtos.models import Addproduto
from oficina import app, db, bcrypt
from .forms import RegistrationForm, LoginFormulario 
from .models import User

# rota da Home Pagina Administrativa
@app.route('/admin')
def admin():
        if 'email' not in session:
            flash(f'Favor fazer seu login primeiro', 'success')
            return redirect(url_for('login'))
        produtos = Addproduto.query.all()
        return render_template ('admin/index.html', title="Página Administrativa", produtos=produtos)

# rota do cadastro de usuario
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():

        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()  #adicionado para salvar no bd       
        flash(f'Obrigado {form.name.data} por registrar', 'success')

        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Registrar Usuários")

    # Rota do Formulario de Login
@app.route('/login',methods=['Get','POST'])
def login():
    form=LoginFormulario(request.form)
    if request.method =="POST" and form.validate():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Olá {form.email.data} voce está logado', 'success')
            return redirect(request.args.get('next')or url_for ('admin'))
        else:
            flash('NÃO FOI POSSIVEL FAZER LOGIN.','danger')
    return render_template ('admin/login.html', form=form, title='Página Login')
   