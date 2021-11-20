from flask import render_template, session, request, redirect, url_for

from oficina import app, db


@app.route('/')
def home():
    return "Controle EZ Confecções"


@app.route('/registrar')
def registrar():
    return render_template('admin/registrar.html', title="Registrar Usuários")
