def media(notas):
    return sum(notas) / len(notas)

def desconto(preco, percentual=10):
    return preco - (preco * percentual / 100)

def estatisticas(notas):
    minimo = min(notas)
    maximo = max(notas)
    media_valor = media(notas)
    return minimo, maximo, media_valor

def situacao(media_valor):
    return "Aprovado" if media_valor >= 6 else "Reprovado"

notas = [7.5, 8.0, 6.0, 5.5]

print("Média:", media(notas))
print("Preço com desconto padrão:", desconto(100))
print("Preço com desconto de 20%:", desconto(100, percentual=20))
print("Estatísticas:", estatisticas(notas))

m = media(notas)
print("Situação:", situacao(m))
