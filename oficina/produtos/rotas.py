from flask import redirect, render_template, url_for, flash, request

from oficina import db,  app
from .models import Fornecedor, Categoria

@app.route('/addfornecedor', methods=['GET', 'POST'])
def addfornecedor():
    
    if request.method =="POST":
        getfornecedor = request.form.get('fornecedor')
        fornecedor = Fornecedor(name=getfornecedor)
        db.session.add(fornecedor)
        flash(f'O Fornecedor {getfornecedor} foi cadastrado com sucesso', 'success')
        db.session.commit
        return redirect(url_for('addfornecedor'))
    return render_template('/produtos/addfornecedor.html', fornecedor='fornecedor')