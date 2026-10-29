import pandas as pd
import numpy as np

# Leitura do arquivo
df = pd.read_csv("pedidos.csv")

# -------------------------
# 1. pedido_grande (np.where)
# -------------------------
df["pedido_grande"] = np.where(df["qtd"] >= 3, "Sim", "Não")

# -------------------------
# 2. perfil (np.select)
# -------------------------
condicoes = [
    df["avaliacao"] >= 5,
    df["avaliacao"] >= 4,
    df["avaliacao"] < 4
]

valores = [
    "cliente_fiel",
    "cliente_regular",
    "cliente_critico"
]

df["perfil"] = np.select(
    condicoes,
    valores,
    default="sem_nota"
)

# -------------------------
# 3. taxa_entrega (.loc)
# -------------------------
df["taxa_entrega"] = "Sem entrega"

df.loc[df["canal"].astype(str).str.contains("Delivery", case=False, na=False),
       "taxa_entrega"] = "Com entrega"

# -------------------------
# 4. faixa_tempo (pd.cut)
# -------------------------
df["faixa_tempo"] = pd.cut(
    df["tempo_entrega_min"],
    bins=[0, 20, 30, 45, float("inf")],
    labels=[
        "Muito rápida",
        "Rápida",
        "Normal",
        "Lenta"
    ]
)

# -------------------------
# Exibir resultados
# -------------------------
print("\nPEDIDO GRANDE")
print(df["pedido_grande"].value_counts())

print("\nPERFIL")
print(df["perfil"].value_counts())

print("\nTAXA ENTREGA")
print(df["taxa_entrega"].value_counts())

print("\nFAIXA TEMPO")
print(df["faixa_tempo"].value_counts())

# Salvar arquivo
df.to_csv("pedidos_classificados.csv", index=False)

print("\nArquivo salvo com sucesso: pedidos_classificados.csv")