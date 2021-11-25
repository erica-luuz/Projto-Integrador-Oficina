from flask import redirect, render_template, url_for, flash, request
from .forms import Addprodutos
from oficina import db,  app, photos
from .models import Fornecedor, Categoria, Addproduto
import secrets

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
        db.session.commit
        return redirect(url_for('addcat'))
    return render_template('/produtos/addfornecedor.html')

# rotas da pagina de cadastro de produtos
@app.route('/addproduto',methods=['GET', 'POST'])
def addproduto():
    fornecedores = Fornecedor.query.all()
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)
    if request.method=="POST":
        
        name = form.name.data
        order_number = form.order_number.data
        unitprice = form.unitprice.data
        total_price = form.total_price.data
        quantity = form.quantity.data
        colors = form.colors.data
        size = form.size.data
        description = form.description.data
        fornecedor = request.form.get('fornecedor')
        categoria = request.form.get('categoria')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")

        addpro = Addproduto(name=name, order_number=order_number, unitprice=unitprice, total_price=total_price, quantity=quantity, colors=colors, size=size, description=description, fornecedor_id=fornecedor, categoria_id=categoria, image_1=image_1)
        db.session.add(addpro)
        flash(f'Produto {name} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
        
        
    return render_template('produtos/addproduto.html', title="Cadastrar Produtos", form=form, fornecedores=fornecedores, categorias=categorias) 
