import pandas as pd
import numpy as np

# Ler o arquivo transformado da atividade anterior
df = pd.read_csv("pedidos.csv")

# Criar pedido_grande com np.where (qtd >= 3)
df["pedido_grande"] = np.where(df["qtd"] >= 3, "Sim", "Não")

# Criar perfil com np.select (3 regras + default 'sem nota')
condicoes = [
    df["avaliacao"] >= 4,
    df["avaliacao"] == 3,
    df["avaliacao"] <= 2
]
valores = ["Bom cliente", "Neutro", "Problema"]
df["perfil"] = np.select(condicoes, valores, default="Sem nota")

# Criar taxa_entrega com .loc
df.loc[df["canal"] == "Delivery", "taxa_entrega"] = "Sim"
df.loc[df["canal"] != "Delivery", "taxa_entrega"] = "Não"

# Criar faixa_tempo com pd.cut (limites: 0, 20, 30, 45, infinito)
bins = [0, 20, 30, 45, float("inf")]
labels = ["Até 20 min", "21-30 min", "31-45 min", "Mais de 45 min"]
df["faixa_tempo"] = pd.cut(df["tempo_entrega_min"], bins=bins, labels=labels)

# Mostrar value_counts de cada coluna criada
print("pedido_grande:\n", df["pedido_grande"].value_counts())
print("perfil:\n", df["perfil"].value_counts())
print("taxa_entrega:\n", df["taxa_entrega"].value_counts())
print("faixa_tempo:\n", df["faixa_tempo"].value_counts())
