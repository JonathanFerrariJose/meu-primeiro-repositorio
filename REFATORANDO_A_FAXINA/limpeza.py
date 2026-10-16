def limpar_nome(nome: str) -> str:

    return nome.strip().title()

def limpar_telefone(telefone: str) -> str:

    numeros = ''.join(filter(str.isdigit, telefone))
    if len(numeros) == 11:
        return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
    return numeros

def limpar_data(data: str) -> str:

    partes = data.strip().split('/')
    if len(partes) == 3:
        dia, mes, ano = partes
        return f"{ano}-{mes.zfill(2)}-{dia.zfill(2)}"
    return data

if __name__ == "__main__":

    print(limpar_nome("  maria da silva "))
    print(limpar_telefone("48 99999-1234"))
    print(limpar_data("16/10/2026"))
