# Importa as bibliotecas necessárias
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash # Para hash de senha e verificação

# ----------------------------------------
# 1. Configuração do Aplicativo Flask
# ----------------------------------------
app = Flask(__name__)

# Chave secreta: O Flask precisa disso para gerenciar sessões e mensagens flash
app.secret_key = 'uma_chave_secreta_muito_forte_para_o_senai' 

# ----------------------------------------
# 2. Configurações de Conexão com o MySQL (XAMPP)
# ----------------------------------------
# Ajuste 'MYSQL_PASSWORD' se você configurou uma senha no XAMPP
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' # Senha padrão vazia no XAMPP
app.config['MYSQL_DB'] = 'americanas_projeto' 

mysql = MySQL(app)


# ----------------------------------------
# 3. Rotas do Aplicativo
# ----------------------------------------

# Rota Principal (Landing Page)
@app.route('/')
def index():
    # Renderiza a página inicial
    return render_template('index.html')

# Rota de Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Captura e trata os dados
        nome = request.form['nome']
        email = request.form['email']
        senha_pura = request.form['senha']
        
        # Segurança: Gera o hash da senha antes de salvar
        senha_hash = generate_password_hash(senha_pura)

        try:
            cur = mysql.connection.cursor()
            # Insere o novo usuário no banco de dados
            cur.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", 
                        (nome, email, senha_hash))
            mysql.connection.commit()
            cur.close()
            
            flash('Cadastro realizado com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))

        except Exception as e:
            # Erro comum: e-mail duplicado ou falha na conexão com o DB
            print(f"Erro ao cadastrar: {e}")
            flash('Erro ao cadastrar. O e-mail pode já estar em uso ou houve um erro de servidor.', 'danger')
            return redirect(url_for('cadastro'))

    return render_template('cadastro.html')

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha_pura = request.form['senha']

        cur = mysql.connection.cursor()
        # Busca o usuário pelo e-mail
        cur.execute("SELECT id, nome, senha FROM usuarios WHERE email = %s", [email])
        usuario = cur.fetchone()
        cur.close()

        if usuario:
            # 1. Checa o hash da senha
            user_id, nome, senha_hash = usuario
            if check_password_hash(senha_hash, senha_pura):
                # 2. Login bem-sucedido: Cria sessão e redireciona
                session['loggedin'] = True
                session['user_id'] = user_id
                session['nome'] = nome
                flash(f'Bem-vindo(a), {nome}!', 'success')
                return redirect(url_for('painel_usuario'))
            else:
                # Senha incorreta
                flash('Email ou senha inválidos.', 'danger')
        else:
            # Usuário não encontrado
            flash('Email ou senha inválidos.', 'danger')

    return render_template('login.html')

# Rota da Página de Sucesso/Painel (Acesso Restrito)
@app.route('/painel_usuario')
def painel_usuario():
    # Verifica se o usuário está logado
    if 'loggedin' in session:
        return render_template('paineldeusuario.html', nome=session['nome'])
    
    # Se não estiver logado, redireciona para o login
    flash('Você precisa fazer login para acessar esta página.', 'danger')
    return redirect(url_for('login'))

# Rota de Logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('nome', None)
    flash('Você saiu da sua conta.', 'success')
    return redirect(url_for('index'))

# Inicializa o Servidor
if __name__ == '__main__':
    app.run(debug=True)