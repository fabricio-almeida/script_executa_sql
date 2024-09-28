import streamlit as st
from config import altera_db
from connections import connections

# Título da aplicação
st.title("Executar SQL em multiplas bases")

# Seletor para escolher a conexão
execute_all = st.checkbox("Executar em todas as conexões")

if not execute_all:
    # Selecione uma única conexão
    connection_name = st.selectbox("Escolha a conexão:", list(connections.keys()))
else:
    connection_name = None  # Para quando todas as conexões forem selecionadas

# Área de texto para inserir o comando SQL
sql_command = st.text_area("Insira seu comando SQL:", height=150)

# Botão para executar o comando
if st.button("Executar"):
    if sql_command:
        if execute_all:
            # Executar o comando em todas as conexões
            for conn_name in connections.keys():
                with st.spinner(f"Executando na conexão: {conn_name}..."):
                    message = altera_db(sql_command, conn_name)  # Obtém a mensagem da execução
                    if "Erro" in message:
                        st.error(f"Erro na conexão {conn_name}: {message}")
                    else:
                        st.success(f"Comando SQL executado com sucesso na conexão: {conn_name}. {message}")
        else:
            # Executa o comando SQL na conexão selecionada
            with st.spinner(f"Executando na conexão {connection_name}..."):
                message = altera_db(sql_command, connection_name)
                if "Erro" in message:
                    st.error(f"Erro na conexão {connection_name}: {message}")
                else:
                    st.success(f"Comando SQL executado com sucesso: {message}")
    else:
        st.error("Por favor, insira um comando SQL.")
