import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# =========================
# CONFIGURAÇÃO
# =========================

st.set_page_config(
    page_title="Crypto Dashboard",
    layout="wide"
)

# Cotação fixa do dólar
DOLAR_BRL = 5.50

# =========================
# CONEXÃO COM BANCO
# =========================

conn = sqlite3.connect("database/crypto.db")

# =========================
# LEITURA DOS DADOS
# =========================

df = pd.read_sql("SELECT * FROM crypto_data", conn)

df["date"] = pd.to_datetime(df["date"])

# =========================
# TÍTULO
# =========================

st.title("📊 Dashboard de Criptomoedas")

# =========================
# FILTRO DE CRIPTO
# =========================

crypto = st.selectbox(
    "Escolha a criptomoeda",
    sorted(df["crypto"].unique())
)

df_crypto = df[df["crypto"] == crypto]

# =========================
# FILTRO DE MOEDA
# =========================

moeda = st.selectbox(
    "Escolha a moeda de exibição",
    ["USD ($)", "BRL (R$)"]
)

# =========================
# FILTRO DE DATA
# =========================

data_escolhida = st.date_input(
    "Escolha uma data",
    value=df_crypto["date"].max()
)

df_dia = df_crypto[
    df_crypto["date"].dt.date == data_escolhida
]

# =========================
# FUNÇÃO DE CONVERSÃO
# =========================

def converter(valor):

    if moeda == "BRL (R$)":
        return valor * DOLAR_BRL

    return valor

# =========================
# FORMATAÇÃO
# =========================

def formatar(valor):

    if moeda == "BRL (R$)":
        return f"R$ {valor:,.2f}"

    return f"$ {valor:,.2f}"

# =========================
# MÉTRICAS GERAIS
# =========================

st.subheader("📈 Métricas Gerais")

maior_preco = converter(df_crypto["high"].max())
menor_preco = converter(df_crypto["low"].min())

col1, col2 = st.columns(2)

col1.metric(
    "Maior preço histórico",
    formatar(maior_preco)
)

col2.metric(
    "Menor preço histórico",
    formatar(menor_preco)
)

# =========================
# DADOS DO DIA
# =========================

st.subheader(f"📅 Dados do dia {data_escolhida}")

if not df_dia.empty:

    linha = df_dia.iloc[0]

    preco = converter(linha["close"])
    preco_max = converter(linha["high"])
    preco_min = converter(linha["low"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Preço de fechamento",
        formatar(preco)
    )

    c2.metric(
        "Preço máximo",
        formatar(preco_max)
    )

    c3.metric(
        "Preço mínimo",
        formatar(preco_min)
    )

    c4.metric(
        "Volume negociado",
        f"{linha['volume']:,.2f}"
    )

else:

    st.warning("Não existem dados para esta data.")

# =========================
# GRÁFICO
# =========================

df_grafico = df_crypto.copy()

if moeda == "BRL (R$)":

    df_grafico["close"] = (
        df_grafico["close"] * DOLAR_BRL
    )

titulo_moeda = "USD ($)"

if moeda == "BRL (R$)":
    titulo_moeda = "BRL (R$)"

fig = px.line(
    df_grafico,
    x="date",
    y="close",
    title=f"Preço histórico - {crypto} ({titulo_moeda})"
)

fig.update_layout(
    xaxis_title="Data",
    yaxis_title="Preço",
    height=500
)

st.plotly_chart(fig, width='stretch')