import numpy as np

notas = np.array([
    [6.5, 7.0, 8.0],
    [5.0, 6.0, 6.5],
    [9.0, 8.5, 9.5],
    [7.5, 7.0, 6.0]
])

medias_alunos = np.round(notas.mean(axis=1), 2)

medias_provas = np.round(notas.mean(axis=0), 2)

status = np.where(medias_alunos >= 7, "Aprovado", "Reprovado")

melhor_aluno = np.argmax(medias_alunos)

print("Médias dos alunos:", medias_alunos)
print("Médias das provas:", medias_provas)
print("Status dos alunos:", status)
print("Aluno com maior média:", melhor_aluno)