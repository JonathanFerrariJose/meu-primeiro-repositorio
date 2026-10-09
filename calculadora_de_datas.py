from datetime import datetime, date

nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")

hoje = date.today()
dias_de_vida = (hoje - nascimento.date()).days
idade = dias_de_vida // 365

dia_semana = nascimento.strftime("%A")

ano_atual = hoje.year
natal = date(ano_atual, 12, 25)
if hoje > natal:
    natal = date(ano_atual + 1, 12, 25)
dias_para_natal = (natal - hoje).days

print(f"Idade aproximada: {idade} anos")
print(f"Você nasceu em uma {dia_semana}")
print(f"Faltam {dias_para_natal} dias para o próximo Natal")
