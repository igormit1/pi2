import mysql.connector
from mysql.connector import Error

def create(nome, usuario, cpf, email, endereco, ocupacao, senha):
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
        INSERT INTO pessoa (Nome, usuario, CPF, Email, Endereco, Ocupacao, Senha)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        
        cursor.execute(comando, (nome, usuario, cpf, email, endereco, ocupacao, senha))
        conexao.commit()
    
    except Error as e:
        print(f'Erro ao conectar ao MySQL: {e}')
        raise  # Relevanta a exceção para ser tratada no submit()
    
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

#-----------------------------------------------

def authenticate(usuario, password):
    try:
        # Conexão ao banco de dados
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='farmacia',
        )
        cursor = conexao.cursor()
        
        # Verifique se o usuario e a senha correspondem
        comando = '''
        SELECT * FROM pessoa WHERE usuario = %s AND Senha = %s
        '''
        cursor.execute(comando, (usuario, password))
        result = cursor.fetchone()
        
        return result is not None  # Retorna True se encontrar um usuário

    except Error as e:
        print(f'Erro ao conectar ao MySQL: {e}')
        return False  # Retorna False em caso de erro

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()