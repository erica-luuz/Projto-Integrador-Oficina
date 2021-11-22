from flask import redirect, render_template, url_for, flash, request

from oficina import db,  app


@app.route('/addfornecedor', methods=['GET', 'POST'])
def addfornecedor():
    return render_template('/produtos/addfornecedor.html')