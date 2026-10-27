import pandas as pd

# Ler os três arquivos
pedidos = pd.read_csv("pedidos.csv")
produtos = pd.read_csv("produtos.csv")
clientes = pd.read_csv("clientes.csv")

# 1. Unir pedidos e produtos (validate='m:1')
ped_prod = pedidos.merge(produtos, on="id_produto", how="left", validate="m:1")
print("Linhas após unir pedidos e produtos:", len(ped_prod))  # deve continuar 687

# 2. Unir resultado com clientes (how='left', indicator=True)
ped_final = ped_prod.merge(clientes, on="id_cliente", how="left", indicator=True)
print("Pedidos sem cliente:", (ped_final["_merge"] == "left_only").sum())

# 3. Criar colunas total e lucro
ped_final["total"] = ped_final["qtd"] * ped_final["preco"]
ped_final["lucro"] = ped_final["qtd"] * (ped_final["preco"] - ped_final["custo"])

# 4. Mostrar lucro por categoria
print(ped_final.groupby("categoria")["lucro"].sum())
