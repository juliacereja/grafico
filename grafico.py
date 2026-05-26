import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title("Análise de Dados do TikTok")

# Ler arquivo CSV
df = pd.read_csv("tiktok_dados_completos.csv")

# Mostrar tabela
st.subheader("Tabela de Dados")
st.dataframe(df)

# Escolher conjunto de dados
opcao = st.selectbox(
    "Escolha um conjunto de dados:",
    df["Dataset"].unique()
)

# Filtrar dados
dados_filtrados = df[df["Dataset"] == opcao]

# Criar gráfico
fig, ax = plt.subplots()

ax.bar(
    dados_filtrados["Categoria"],
    dados_filtrados["Valor"]
)

# Ajustes
ax.set_title(opcao)
ax.set_xlabel("Categoria")
ax.set_ylabel(dados_filtrados["Unidade"].iloc[0])

plt.xticks(rotation=45)

# Mostrar gráfico
st.pyplot(fig)
