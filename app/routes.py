from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo='Página Inicial')

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo='Contato')