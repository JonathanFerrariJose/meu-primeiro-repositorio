
def e_bissexto(ano: int) -> bool:

    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def calcular_imc(peso: float, altura: float) -> float:

    return peso / (altura ** 2)

if __name__ == "__main__":

    anos = [2000, 1900, 2024, 2023]
    for ano in anos:
        print(f"Ano {ano} é bissexto? {e_bissexto(ano)}")

    print(f"IMC (70kg, 1.75m): {calcular_imc(70, 1.75):.2f}")
    print(f"IMC (90kg, 1.80m): {calcular_imc(90, 1.80):.2f}")
