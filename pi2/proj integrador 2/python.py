from flask import Flask, request, render_template

app = Flask(__name__)

# Rota para servir o arquivo HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o formulário
@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['full-name']
    cpf = request.form['cpf']
    email = request.form['email']
    endereco = request.form['address']
    ocupacao = request.form['occupation']
    senha = request.form['password']
    confirmaSenha = request.form['confirm-password']
    
    # Aqui você pode manipular ou salvar os dados
    print(f'Nome: {nome}, CPF: {cpf}, Email: {email}, Endereço: {endereco}, Ocupação: {ocupacao}, Senha: {senha}')

    create(nome, cpf, email, endereco, ocupacao, senha)
    
    return f'Cadastro realizado com sucesso! Bem-vindo(a), {nome}.'

if __name__ == '__main__':
    app.run(debug=True)

#-----------------------------------------------------------------------------------------------------------------------

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='farmacia',
)
cursor = conexao.cursor()

def create(nome1, cpf1, email1, endereco1, ocupacao1, senha1):        
    comando = f'''
    INSERT INTO pessoa (Nome, CPF, email, Endereco, Ocupacao, Senha)
    VALUES ('{nome1}', '{cpf1}', '{email1}', '{endereco1}', '{ocupacao1}', '{senha1}')
    '''

    cursor.execute(comando)
    conexao.commit() # edita o banco de dados

#-------------------------------------------------------------------------------

def read():        
    comando = f'SELECT * FROM pessoa'

    cursor.execute(comando)

    resultado = cursor.fetchall() # ler o banco de dados

    print(resultado)

#-------------------------------------------------------------------------------


def update():       
    nome_pessoa = "aaaaa"

    ocupacao_pessoa = "GERENTE"

    comando = f'UPDATE pessoa SET nome = "{nome_pessoa}" WHERE ocupacao = "{ocupacao_pessoa}"'

    cursor.execute(comando)

    conexao.commit() 

#-------------------------------------------------------------------------------

def delete():        
    nome1 = "Markin"

    comando = f'DELETE FROM Pessoa WHERE nome = "{nome1}"'

    cursor.execute(comando)

    conexao.commit() # edita o banco de dados



cursor.close()
conexao.close()

#--------------------------------------------
#Para verificar a senha durante o login:
#SELECT * FROM Pessoa
#WHERE CPF = '12345678901' AND Senha = SHA2('minha_senha_segura', 256);