import streamlit as st

# Configurar a página com título e layout
st.set_page_config(
    page_icon="",
    page_title="Jogadores",
    layout="wide"
)

# Carregar os dados da sessão do home
df_data = st.session_state["data"]

# Obter os clubes disponíveis no conjunto de dados
clubes = df_data["Club"].value_counts().index

# Criar um dropdown na barra lateral para selecionar um clube
club = st.sidebar.selectbox("Clube", clubes)

# Filtrar os dados dos jogadores com base no clube selecionado
df_players = df_data[df_data["Club"] == club]
# Obter os jogadores disponíveis para o clube selecionado
players = df_players["Name"].value_counts().index
# Criar um dropdown na barra lateral para selecionar um jogador
player = st.sidebar.selectbox("Jogador", players)

# Obter estatísticas do jogador selecionado
player_stats = df_data[df_data["Name"] == player].iloc[0]

# Exibir a imagem do jogador
st.image(player_stats["Photo"])
# Exibir o nome do jogador como título
st.title(f"{player_stats['Name']}")

# Exibir informações sobre o jogador (clube e posição)
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

# Criar colunas para exibir informações adicionais
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")

# Inserir uma linha divisória
st.divider()
# Exibir o título "Overall" e uma barra de progresso
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

# Criar colunas para exibir métricas como valor de mercado, remuneração semanal e cláusula de rescisão
col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£{player_stats['Value(£)']:,.2f}")
col2.metric(label="Remuneração Semanal", value=f"£{player_stats['Wage(£)']:,.2f}")
col3.metric(label="Cláusula de Rescisão", value=f"£{player_stats['Release Clause(£)']:,.2f}")