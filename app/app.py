from flask import Flask, render_template, request, redirect, jsonify
from services.CarregaProduto import CarregaProduto
from services.Carrinho import Carrinho

carrinho = Carrinho()
app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/management')
def management():
    return render_template('management.html')


@app.route('/management/product')
def product():
    products = CarregaProduto.LoadProduto(app.root_path)
    return render_template('product.html', products=products)


@app.route('/management/product/create', methods=['POST'])
def product_create():
    name = request.form['product-name']
    price = request.form['product-price']
    # FUNCIONALIDADE DE CADASTRAR PRODUTO #######################
    print(name, price)
    return redirect('/management/product')


@app.route('/management/product/update', methods=['POST'])
def product_update():
    name = request.form['product-name']
    price = request.form['product-price']
    productId = request.form['product-id']
    # FUNCIONALIDADE DE ATUALIZAR PRODUTO #########################
    print(name, price, productId)
    return redirect('/management/product')


@app.route('/management/product/remove', methods=['POST'])
def product_remove():
    productId = request.form['product-id']
    # FUNCIONALIDADE DE REMOVER ##########################
    print(productId)
    return redirect('/management/product')


@app.route('/marketplace')
def marketplace():
    products = CarregaProduto.LoadProduto(app.root_path)
    return render_template('marketplace.html', products=products)


@app.route('/marketplace_add', methods=['POST'])
def marketplace_add():
    product = request.form['product']
    carrinho.adiciona_produto(product)
    print(carrinho.get_items())
    return '', 204


@app.route('/marketplace_remove', methods=['POST'])
def marketplace_remove():
    product = request.form['product']
    carrinho.remove_produto(product)
    print(carrinho.get_items())
    return '', 204


if (__name__ == '__main__'):
    app.run()
