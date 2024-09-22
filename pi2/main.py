from flask import Flask, request, render_template
from dao import create
from dao import authenticate

app = Flask(__name__)

#----------------------------------------------------------

# principal
@app.route('/')
def index():
    return render_template('index.html')

#----------------------------------------------------------

#registro
@app.route('/register')
def register():
    return render_template('register.html')

#----------------------------------------------------------

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        password = request.form['password']
        
        if authenticate(usuario, password):
            return render_template('logado.html', usuario=usuario)
        else:
            return "Credenciais inválidas. Tente novamente."
    
    return render_template('login.html')

#----------------------------------------------------------

#registro
@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['full-name']
    usuario = request.form['username']
    cpf = request.form['cpf']
    email = request.form['email']
    endereco = request.form['address']
    ocupacao = request.form['occupation']
    senha = request.form['password']

    try:
        create(nome, usuario, cpf, email, endereco, ocupacao, senha)
        return f'Cadastro realizado com sucesso! Bem-vindo(a), {usuario}.'
    except Exception as e:
        return f'Ocorreu um erro: {str(e)}'
    
#----------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
