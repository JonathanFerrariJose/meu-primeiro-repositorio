import pandas as pd
import numpy as np

def preparar_pedidos(pedidos, produtos, clientes):
    # unir pedidos e produtos
    ped_prod = pedidos.merge(produtos, on="id_produto", how="left", validate="m:1")

    # unir com clientes
    ped_final = ped_prod.merge(clientes, on="id_cliente", how="left", validate="m:1")

    # criar colunas pedido_grande e perfil com assign
    ped_final = ped_final.assign(
        pedido_grande = np.where(ped_final["qtd"] >= 3, "Sim", "Não"),
        perfil = np.select(
            [
                ped_final["avaliacao"] >= 4,
                ped_final["avaliacao"] == 3,
                ped_final["avaliacao"] <= 2
            ],
            ["Bom cliente", "Neutro", "Problema"],
            default="Sem nota"
        )
    )

    return ped_final

# Ler os arquivos
pedidos = pd.read_csv("pedidos.csv")
produtos = pd.read_csv("produtos.csv")
clientes = pd.read_csv("clientes.csv")

# Executar pipeline
resultado = preparar_pedidos(pedidos, produtos, clientes)

# Salvar resultado
resultado.to_csv("pedidos_prontos.csv", index=False)

# Mostrar shape e head
print("Shape:", resultado.shape)
print(resultado.head())
