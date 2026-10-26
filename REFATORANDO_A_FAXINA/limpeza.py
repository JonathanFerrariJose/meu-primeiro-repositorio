"""
Módulo de funções de limpeza de dados.
"""

def limpar_nome(nome: str) -> str:
    """
    Remove espaços extras e coloca o nome em formato título.
    """
    return nome.strip().title()

def limpar_telefone(telefone: str) -> str:
    """
    Remove caracteres não numéricos e formata como (XX) XXXXX-XXXX.
    """
    numeros = ''.join(filter(str.isdigit, telefone))
    if len(numeros) == 11:
        return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
    return numeros

def limpar_data(data: str) -> str:
    """
    Converte datas no formato DD/MM/AAAA para AAAA-MM-DD.
    """
    partes = data.strip().split('/')
    if len(partes) == 3:
        dia, mes, ano = partes
        return f"{ano}-{mes.zfill(2)}-{dia.zfill(2)}"
    return data

if __name__ == "__main__":
    # Testes rápidos
    print(limpar_nome("  maria da silva "))
    print(limpar_telefone("48 99999-1234"))
    print(limpar_data("16/10/2026"))