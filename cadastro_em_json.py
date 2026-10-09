import json

contatos = [
    {"nome": "Ana Silva", "telefone": "1111-1111", "cidade": "Florianópolis"},
    {"nome": "Bruno Costa", "telefone": "2222-2222", "cidade": "São Paulo"},
    {"nome": "Carla Souza", "telefone": "3333-3333", "cidade": "Florianópolis"},
    {"nome": "Diego Lima", "telefone": "4444-4444", "cidade": "Rio de Janeiro"}
]

with open("contatos.json", "w", encoding="utf-8") as f:
    json.dump(contatos, f, indent=2, ensure_ascii=False)

with open("contatos.json", "r", encoding="utf-8") as f:
    lista_lida = json.load(f)

cidade_escolhida = "Florianópolis"
print(f"Contatos de {cidade_escolhida}:")
for contato in lista_lida:
    if contato["cidade"] == cidade_escolhida:
        print(contato)
