def so_digitos(texto):
    return ''.join(filter(str.isdigit, texto))
def normalizar_nome(nome):
    return nome.strip().title()
def formatar_data(texto):
    dia, mes, ano = texto.strip('/').split('/')
    return f"{ano}/{mes}/{dia}"
if __name__ == "__main__":
    print (so_digitos("abc44843def4150"))
    print (normalizar_nome("  Jonathan Ferrari  "))
    print (formatar_data("10/12/1964"))
