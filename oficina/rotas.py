from flask import render_template, session, Request, url_for

from oficina import app, db


@app.route('/')

def home():
    return "Controle EZ Confecções"