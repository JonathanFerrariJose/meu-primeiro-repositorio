alunos = [
    {"nome": "Jonathan", "nota": 8.5},
    {"nome": "Andre", "nota": 6.0},
    {"nome": "Thiago", "nota": 7.2},
    {"nome": "Wilton", "nota": 9.0}
]
aprovados = 0
for aluno in alunos:
    if aluno["nota"] >= 7:
        print(f"{aluno['nome']} foi aprovado com nota {aluno['nota']}")
        aprovados += 1
print(f"Total de alunos aprovados: {aprovados}")