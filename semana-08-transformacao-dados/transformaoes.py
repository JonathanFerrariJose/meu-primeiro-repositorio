import pandas as pd

# Ler o arquivo pedidos.csv
df = pd.read_csv("pedidos.csv")

# Converter coluna de data
df["data"] = pd.to_datetime(df["data"], errors="coerce")

# Criar colunas mes e dia_semana
df["mes"] = df["data"].dt.month
df["dia_semana"] = df["data"].dt.dayofweek  # 0 = segunda, 6 = domingo

# Padronizar canal
df["canal"] = df["canal"].str.strip().str.title()
print(df["canal"].value_counts())  # devem sobrar 3 canais

# Criar coluna dia (seg a dom)
dias_map = {
    0: "Segunda",
    1: "Terça",
    2: "Quarta",
    3: "Quinta",
    4: "Sexta",
    5: "Sábado",
    6: "Domingo"
}
df["dia"] = df["dia_semana"].map(dias_map)

# Criar coluna faixa_entrega com função e apply
def faixa_entrega(minutos):
    try:
        minutos = int(minutos)
        if minutos <= 30:
            return "Rápida"
        elif minutos <= 60:
            return "Normal"
        else:
            return "Demorada"
    except:
        return "Indefinido"

df["faixa_entrega"] = df["tempo_entrega_min"].apply(faixa_entrega)

# Visualizar resultado
print(df.head())
