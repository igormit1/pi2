from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# Rota para servir o arquivo HTML
@app.route('/')
def index():
    return render_template('register.html')

# Rota para processar o formulário
@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['full-name']
    cpf = request.form['cpf']
    email = request.form['email']
    endereco = request.form['address']
    ocupacao = request.form['occupation']
    senha = request.form['password']
    
    # Aqui você pode manipular ou salvar os dados
    print(f'Nome: {nome}, CPF: {cpf}, Email: {email}, Endereço: {endereco}, Ocupação: {ocupacao}, Senha: {senha}')

    try:
        create(nome, cpf, email, endereco, ocupacao, senha)
        return f'Cadastro realizado com sucesso! Bem-vindo(a), {nome}.'
    except Exception as e:
        return f'Ocorreu um erro: {str(e)}'

def create(nome1, cpf1, email1, endereco1, ocupacao1, senha1):        
    try:
        # Conexão ao banco de dados
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='farmacia',
        )
        cursor = conexao.cursor()

        comando = '''
        INSERT INTO pessoa (Nome, CPF, Email, Endereco, Ocupacao, Senha)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        
        # Execução do comando com parâmetros
        cursor.execute(comando, (nome1, cpf1, email1, endereco1, ocupacao1, senha1))
        conexao.commit()
    
    except Error as e:
        print(f'Erro ao conectar ao MySQL: {e}')
        raise  # Relevanta a exceção para ser tratada no submit()
    
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

if __name__ == '__main__':
    app.run(debug=True)