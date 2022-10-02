from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/management')
def management():
    return render_template('management.html')


@app.route('/management/register')
def register():
    return render_template('register.html')


@app.route('/management/register/new', methods=['POST'])
def register_new():
    name = request.form['name']
    price = request.form['price']
    # FUNCIONALIDADE DE CADASTRAR PRODUTO
    print(name)
    return redirect('/management/register')


if (__name__ == '__main__'):
    app.run()
