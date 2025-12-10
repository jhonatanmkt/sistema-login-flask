import mysql.connector
from mysql.connector import Error

# --------------------------------------------------
# Coloque aqui as MESMAS credenciais do seu app.py
HOST_DB = 'localhost'
USUARIO_DB = 'root'
SENHA_DB = ''  # Deixe em branco se for a senha padrão do XAMPP
NOME_DB = 'americanas_projeto'
# --------------------------------------------------

def testar_conexao():
    """Tenta se conectar ao banco de dados MySQL."""
    try:
        # Tenta estabelecer a conexão
        conexao = mysql.connector.connect(
            host=HOST_DB,
            user=USUARIO_DB,
            password=SENHA_DB,
            database=NOME_DB
        )

        # Se a conexão foi bem-sucedida
        if conexao.is_connected():
            print("------------------------------------------")
            print("✅ CONEXÃO BEM-SUCEDIDA!")
            print("------------------------------------------")
            print(f"Conectado ao banco de dados: '{NOME_DB}'")
            
            # Tenta verificar a tabela 'usuarios'
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuarios LIMIT 1;")
            print("Tabela 'usuarios' encontrada e acessível.")
            cursor.close()

    except Error as e:
        # Se a conexão falhar
        print("------------------------------------------")
        print("❌ FALHA NA CONEXÃO.")
        print("------------------------------------------")
        
        if e.errno == 1045:
            print("ERRO: 'Access denied' (Acesso negado).")
            print("Verifique se o usuário 'root' e a senha (SENHA_DB) estão corretos.")
            
        elif e.errno == 1049:
            print(f"ERRO: Banco de dados '{NOME_DB}' não encontrado.")
            print("Verifique se o nome do banco (NOME_DB) está correto.")
            
        elif e.errno == 1146:
            print("ERRO: Tabela 'usuarios' não existe ('Table doesn't exist').")
            print("Execute o script SQL para criar a tabela no phpMyAdmin.")

        elif e.errno == 2003:
             print("ERRO: Não foi possível se conectar ao 'localhost'.")
             print("Verifique se o XAMPP (MySQL) está LIGADO.")
             
        else:
            # Outros erros
            print(f"Erro inesperado: {e}")

    finally:
        # Fecha a conexão se ela foi aberta
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
            print("\nConexão fechada.")

# Executa a função de teste
if __name__ == "__main__":
    testar_conexao()