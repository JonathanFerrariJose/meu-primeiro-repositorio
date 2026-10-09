import csv

with open("notas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nome", "nota1", "nota2"])
    writer.writeheader()
    writer.writerows([
        {"nome": "Jonathan", "nota1": 8.0, "nota2": 7.5},
        {"nome": "Thiago", "nota1": 6.0, "nota2": 5.5},
        {"nome": "Andre", "nota1": 9.0, "nota2": 8.5},
        {"nome": "Wilsom", "nota1": 4.0, "nota2": 6.0},
        {"nome": "Natan", "nota1": 7.0, "nota2": 7.0},
    ])

resultados = []
with open("notas.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for linha in reader:
        nome = linha["nome"]
        nota1 = float(linha["nota1"])
        nota2 = float(linha["nota2"])
        media = (nota1 + nota2) / 2
        situacao = "Aprovado" if media >= 7 else "Reprovado"
        resultados.append({"nome": nome, "media": round(media, 2), "situacao": situacao})

with open("resultado.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nome", "media", "situacao"])
    writer.writeheader()
    writer.writerows(resultados)

print("Processo concluído! Arquivo resultado.csv gerado com sucesso.")