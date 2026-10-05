contatos = [
    {"nome": "Ana", "telefone": "1111-1111", "email": "ana@email.com"},
    {"nome": "Bruno", "telefone": "2222-2222", "email": "bruno@email.com"},
    {"nome": "Carla", "telefone": "3333-3333", "email": "carla@email.com"},
    {"nome": "Daniel", "telefone": "4444-4444", "email": "daniel@email.com"},
    {"nome": "Eduarda", "telefone": "5555-5555", "email": "eduarda@email.com"},
]

def buscar_contato(nome):
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            return contato
    return None

if __name__ == "__main__":
    nome_busca = input("Digite o nome do contato: ")
    resultado = buscar_contato(nome_busca)
    if resultado:
        print("Contato encontrado:", resultado)
    else:
        print("Contato não encontrado.")
