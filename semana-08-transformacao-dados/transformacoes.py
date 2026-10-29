import pandas as pd
import os

# Mostrar diretório atual
print("Diretório atual:")
print(os.getcwd())

# Caminho do arquivo
arquivo = "pedidos.csv"

# Ler CSV
df = pd.read_csv(arquivo)

# Converter data
df["data"] = pd.to_datetime(df["data"])

# Criar coluna mês
df["mes"] = df["data"].dt.month

# Criar coluna dia_semana
df["dia_semana"] = df["data"].dt.day_name()

# Mapear dia da semana
mapa_dias = {
    "Monday": "seg",
    "Tuesday": "ter",
    "Wednesday": "qua",
    "Thursday": "qui",
    "Friday": "sex",
    "Saturday": "sab",
    "Sunday": "dom"
}

df["dia"] = df["dia_semana"].map(mapa_dias)

# Padronizar canal
df["canal"] = (
    df["canal"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("\nContagem dos canais:")
print(df["canal"].value_counts())

# Criar faixa_entrega
def faixa_entrega(tempo):
    if pd.isna(tempo):
        return "Sem informação"
    elif tempo <= 20:
        return "Rápida"
    elif tempo <= 40:
        return "Normal"
    else:
        return "Lenta"

df["faixa_entrega"] = df["tempo_entrega_min"].apply(faixa_entrega)

# Salvar resultado
df.to_csv("pedidos_tratados.csv", index=False)

print("\nArquivo salvo com sucesso!")
print("pedidos_tratados.csv")