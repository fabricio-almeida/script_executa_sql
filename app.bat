@echo off
:: Ativar o ambiente virtual
call Scripts\activate

:: Executar o Streamlit
streamlit run app.py

:: Manter a janela aberta após a execução (opcional)
pause
