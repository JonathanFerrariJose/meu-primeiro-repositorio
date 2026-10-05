cadastro = {
    "nome": "Jonathan",
    "idade": 36,
    "cidade": "Florianópolis",
    "profissão": "Estudante"
}

cadastro.update({"email": "jonathanferrari@sctec.com"})

print(cadastro)

for chave, valor in cadastro.items():
    print(f"{chave}: {valor}")