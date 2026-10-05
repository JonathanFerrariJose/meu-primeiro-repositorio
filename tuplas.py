dias = ("segunda-feira", "terça-feira", "quarta-feira")
print("Tupla inicial:", dias)

dias_lista = list(dias)
print("Lista:", dias_lista)

dias_lista.append("domingo")
print("Lista após adicionar:", dias_lista)

dias = tuple(dias_lista)
print("Tupla final:", dias)