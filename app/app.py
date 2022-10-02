from flask import Flask, render_template, request, redirect


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
    return render_template('product.html')


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
    id = request.form['product-id']
    # FUNCIONALIDADE DE ATUALIZAR PRODUTO #########################
    print(name, price, id)
    return redirect('/management/product')


@app.route('/management/product/remove', methods=['POST'])
def product_remove():
    id = request.form('product-id')
    # FUNCIONALIDADE DE REMOVER ##########################
    return redirect('/management/product')


if (__name__ == '__main__'):
    app.run()
