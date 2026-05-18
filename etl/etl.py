import pandas as pd
import os
import sqlite3

# Caminho da pasta com os CSVs
pasta = "data/raw"

# Lista para armazenar os DataFrames
lista_df = []

# Percorrer todos os arquivos CSV
for arquivo in os.listdir(pasta):

    if arquivo.endswith(".csv"):

        caminho_arquivo = os.path.join(pasta, arquivo)

        # Ler CSV
        df = pd.read_csv(caminho_arquivo)

        # Converter data
        df["date"] = pd.to_datetime(df["date"])

        # Criar coluna com nome da moeda
        df["crypto"] = arquivo.replace(".csv", "")

        # Adicionar na lista
        lista_df.append(df)

# Unir todos os DataFrames
df_final = pd.concat(lista_df)

# Remover valores nulos
df_final.dropna(inplace=True)

# Salvar CSV tratado
df_final.to_csv(
    "data/processed/crypto_data.csv",
    index=False
)

# Criar banco SQLite
conn = sqlite3.connect("database/crypto.db")

# Salvar tabela no banco
df_final.to_sql(
    "crypto_data",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("ETL concluído com sucesso!")
print(df_final.head())