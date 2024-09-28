
# Importação de bibliotecas necessarias
import psycopg2
from connections import connections

# Funções

# Função para criar conexão com o banco
def conecta_db(connection_name):
 try:
    host, database, user, password = connections[connection_name]
    conn = psycopg2.connect(
              host=host,
              database=database,
              user=user,
              password=password
    )
    return conn     
 except Exception as error:
        print("Erro ao conectar ao banco de dados:", error)
        return None
      
def altera_db(sql, connection_name):
    """Executa uma alteração ou consulta no banco de dados e retorna mensagens de status."""
    conn = None  # Inicializa a variável de conexão
    try:
        conn = conecta_db(connection_name)  # Passa os parâmetros necessários
        with conn:  # Gerenciador de contexto para a conexão
            with conn.cursor() as cur:  # Gerenciador de contexto para o cursor
                cur.execute(sql)  # Executa a consulta
                # Verifica se é uma consulta SELECT e retorna os resultados
                if sql.strip().upper().startswith("SELECT"):
                    results = cur.fetchall()
                    return f"Consulta executada com sucesso. Resultados: {results}"
                else:
                    conn.commit()  # Comita a transação
                    return 'Código executado com sucesso.'  # Mensagem de sucesso
    except Exception as error:
        return f"Erro ao executar o código no banco de dados: {error}"  # Mensagem de erro
    finally:
        if conn is not None:
            conn.close()  # Garante que a conexão seja fechada
