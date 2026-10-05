with open("diario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Hoje comecei meu diário.\n")
    arquivo.write("Estou praticando Python.\n")
    arquivo.write("Também vou usar GitHub.\n")

with open("diario.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Agora estou aprendendo sobre arquivos.\n")
    arquivo.write("E também sobre versionamento.\n")

with open("diario.txt", "r", encoding="utf-8") as arquivo:
    for i, linha in enumerate(arquivo, start=1):
        print(f"{i}: {linha.strip()}")