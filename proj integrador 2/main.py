from flask import Flask, request, render_template

app = Flask(__name__)

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
    confirmaSenha = request.form['confirm-password']
    
    # Aqui você pode manipular ou salvar os dados
    print(f'Nome: {nome}, CPF: {cpf}, Email: {email}, Endereço: {endereco}, Ocupação: {ocupacao}, Senha: {senha}')
    
    return f'Cadastro realizado com sucesso! Bem-vindo(a), {nome}.'

if __name__ == '__main__':
    app.run(debug=True)

#-----------------------------------------------------------------------------------------------------------------------

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='teste',
)
cursor = conexao.cursor()

print()

# CREATE

# nome_produto = "chocolate"

# valor = 15

# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados



# READ

# comando = f'SELECT * FROM vendas'

# cursor.execute(comando)

# resultado = cursor.fetchall() # ler o banco de dados

# print(resultado)



# UPDATE

# nome_produto = "todynho"

# valor = 6

# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados



# DELETE

# nome_produto = "todynho"

# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados

cursor.close()
conexao.close()