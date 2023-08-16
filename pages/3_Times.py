import streamlit as st

# Configurar a página com título e layout
st.set_page_config(
    page_icon="",
    page_title="Times",
    layout="wide"
)

# Carregar os dados da sessão do home
df_data = st.session_state["data"]

# Obter os clubes disponíveis no conjunto de dados
clubes = df_data["Club"].value_counts().index
# Criar um dropdown na barra lateral para selecionar um clube
club = st.sidebar.selectbox("Clube", clubes)

# Filtrar os dados dos jogadores para o clube selecionado, criar índice e ordenar pelo "Overall"
df_filtered = df_data[df_data["Club"] == club].set_index("Name").sort_values("Overall", ascending=False)

# Exibir o logo do clube e o nome do clube como título
st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

# Colunas a serem exibidas na tabela
columns = ["Age", "Photo", "Flag", "Overall", "Value(£)","Wage(£)",
           "Joined","Height(cm.)","Weight(lbs.)","Contract Valid Until","Release Clause(£)"]

# Exibir os dados em um dataframe customizado
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                 "Value(£)": st.column_config.NumberColumn(format="£%f"),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()),
                 "Photo": st.column_config.ImageColumn(width="small"),
                 "Flag": st.column_config.ImageColumn("Country", width="small"),
                 "Contract Valid Until": st.column_config.NumberColumn(format="%d")
             })