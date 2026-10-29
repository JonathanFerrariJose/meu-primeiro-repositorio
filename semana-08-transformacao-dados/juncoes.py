import pandas as pd

# ==========================
# Leitura dos arquivos
# ==========================

pedidos = pd.read_csv("pedidos.csv")
produtos = pd.read_csv("produtos.csv")
clientes = pd.read_csv("clientes.csv")

print("Pedidos:", pedidos.shape)
print("Produtos:", produtos.shape)
print("Clientes:", clientes.shape)

# ==========================
# Junção pedidos + produtos
# ==========================

df = pedidos.merge(
    produtos,
    on="id_produto",
    how="left",
    validate="m:1"
)

print("\nLinhas após merge com produtos:")
print(len(df))

# Deve continuar com 687 linhas
print(df.shape)

# ==========================
# Junção com clientes
# ==========================

df = df.merge(
    clientes,
    on="id_cliente",
    how="left",
    indicator=True
)

print("\nOrigem dos registros:")
print(df["_merge"].value_counts())

# Quantos pedidos ficaram sem cliente

sem_cliente = (df["_merge"] == "left_only").sum()

print("\nPedidos sem cliente:")
print(sem_cliente)

# ==========================
# Total e Lucro
# ==========================

df["total"] = df["qtd"] * df["preco"]

df["lucro"] = df["qtd"] * (
    df["preco"] - df["custo"]
)

# ==========================
# Lucro por categoria
# ==========================

print("\nLucro por categoria:")

print(
    df.groupby("categoria")["lucro"]
      .sum()
      .sort_values(ascending=False)
)

# ==========================
# Salvar resultado
# ==========================

df.to_csv(
    "pedidos_enriquecidos.csv",
    index=False
)

print("\nArquivo salvo:")
print("pedidos_enriquecidos.csv")