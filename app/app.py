from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/management')
def management():
    return render_template('management.html')


if (__name__ == '__main__'):
    app.run()