# Importar as bibliotecas necessárias
import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

# Verificar se a variável "data" não existe na sessão do Streamlit
if "data" not in st.session_state:

    # Carregar os dados do arquivo CSV e fazer filtragens
    df_data = pd.read_csv("dataset/CLEAN_FIFA23_official_data.csv", index_col = 0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"]> 0]
    df_data = df_data.sort_values(by="Overall", ascending = False)

    # Armazenar os dados filtrados na sessão do Streamlit
    st.session_state["data"] = df_data

st.write("# FIFA 23 OFFICIAL DATASET! ")

# Barra lateral com informações do desenvolvedor
st.sidebar.markdown("Desenvolvimento teste")

# Botão para acessar os dados no Kaggle
btn = st.button("Acessar os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/sanjeetsinghnaik/fifa-23-players-dataset")

st.markdown(
    """
    A FIFA 23, o último título da série desenvolvida pela EA Sports e publicado pela Electronic Arts, é um jogo de simulação de futebol lançado em setembro de 2022 para várias plataformas. 
    Além de recriar a atmosfera do futebol, o jogo se destaca por analisar minuciosamente detalhes 
    dos jogadores.
     
    Através das informações presentes nas colunas de dados, como idade, nacionalidade, classificação geral, 
    potencial de crescimento, clube atual, habilidades, preferências e atributos físicos, os jogadores podem mergulhar em uma experiência rica e realista, 
    explorando nuances que podem definir o sucesso ou fracasso dentro do jogo. 
    
    Essa abordagem meticulosa proporciona uma imersão mais profunda e 
    reflete a crescente importância da análise de desempenho no futebol contemporâneo.
    """
    )

