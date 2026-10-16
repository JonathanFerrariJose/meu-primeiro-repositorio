alunos = [
    {"nome": "Jonathan", "nota": 8.5},
    {"nome": "Andre", "nota": 7.0},
    {"nome": "Nata", "nota": 9.0},
    {"nome": "Arthur", "nota": 6.5},
    {"nome": "Sergio", "nota": 7.5}
]

ordenados = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)

print("Ordenados (do maior para o menor):")
for aluno in ordenados:
    print(f"Aluno: {aluno['nome']}, Nota: {aluno['nota']}")

aprovados = list(filter(lambda aluno: aluno["nota"] >= 7.0, alunos))

print("\nAprovados (nota >= 7):")
for aluno in aprovados:
    print(f"Aluno: {aluno['nome']}, Nota: {aluno['nota']}")