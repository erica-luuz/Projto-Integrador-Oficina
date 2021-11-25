from flask import redirect, render_template, url_for, flash, request
from .forms import Addprodutos
from oficina import db,  app, photos
from .models import Fornecedor, Categoria
# rotas da pag de cadastro de fornecedor.
@app.route('/addfornecedor', methods=['GET', 'POST'])
def addfornecedor():
    
    if request.method =="POST":
        getfornecedor = request.form.get('fornecedor')
        fornecedor = Fornecedor(name=getfornecedor)
        db.session.add(fornecedor)
        flash(f'O Fornecedor {getfornecedor} foi cadastrado com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addfornecedor'))
    return render_template('/produtos/addfornecedor.html', fornecedor='fornecedor')


# rotas da pag de cadastro de categoria

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    
    if request.method =="POST":
        getfornecedor = request.form.get('categoria')
        cat = Categoria(name=getfornecedor)
        db.session.add(cat)
        flash(f'A Categoria {getfornecedor} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('/produtos/addfornecedor.html')

# rotas da pagina de cadastro de produtos
@app.route('/addproduto',methods=['GET', 'POST'])
def addproduto():
    fornecedores = Fornecedor.query.all()
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)
    if request.method=="POST":
        photos.save(request.files.get('image_1'))
        photos.save(request.files.get('image_2'))
        db.session.commit()
    return render_template('produtos/addproduto.html', title="Cadastrar Produtos", form=form, fornecedores=fornecedores, categorias=categorias) 
