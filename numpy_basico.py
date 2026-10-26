import numpy as np

matriz = np.arange(1, 13).reshape(3, 4)
print("Matriz:\n", matriz)

print("Shape:", matriz.shape)
print("Ndim:", matriz.ndim)
print("Size:", matriz.size)

print("Segunda linha:", matriz[1])
print("Última coluna:", matriz[:, -1])
print("Bloco central:\n", matriz[0:2, 1:3])

pares = matriz[matriz % 2 == 0]
print("Valores pares:", pares)
print("Quantidade de pares:", pares.size)
