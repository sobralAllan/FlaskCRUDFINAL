from app import app
from flask import render_template
from flask import request
import json
import requests
link = "https://flaskti18n-default-rtdb.firebaseio.com/" #Conecta o banco
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo='Página Inicial')

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo='Contato')

@app.route('/cadastro')
def cadastrar():
    return render_template('cadastro.html', titulo='Cadastro')

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf      = request.form.get("cpf")
        nome     = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados    = {"cpf":cpf,"nome":nome,"telefone":telefone,"endereco":endereco}
        requisicao = requests.post(f'{link}/cadastrar/.json', data=json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #Solicitar os dados
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        for codigo in dicionario:
            usuario = dicionario[codigo]['cpf']
            if usuario == "1231":
                idCadastro = codigo
        return idCadastro
    except Exception as e:
        return f'Algo deu errado!\n\n + {e}'

# -NySMWeGqu5v3xAyI1B_
@app.route('/atualizar')
def atualizar():
    try:
        dados = {"telefone":"999999999"}#Parâmetro para atualização
        requisicao = requests.patch(f'{link}/cadastrar/-NySMwfgLGHk_RWHz7PK/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Houve um erro!\n\n + {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-NySMWeGqu5v3xAyI1B_/.json')
        return "Excluido com sucesso!"
    except Exception as e:
        return f'Houve um erro\n\n + {e}'
