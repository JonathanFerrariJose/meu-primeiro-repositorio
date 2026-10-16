import csv
from limpeza import limpar_nome, limpar_telefone, limpar_data

def processar_csv(entrada: str, saida: str):

    with open(entrada, newline='', encoding='utf-8') as f_in, \
         open(saida, 'w', newline='', encoding='utf-8') as f_out:
        
        leitor = csv.DictReader(f_in)
        campos = leitor.fieldnames
        escritor = csv.DictWriter(f_out, fieldnames=campos)
        escritor.writeheader()

        for linha in leitor:
            linha['nome'] = limpar_nome(linha['nome'])
            linha['telefone'] = limpar_telefone(linha['telefone'])
            linha['data'] = limpar_data(linha['data'])
            escritor.writerow(linha)

if __name__ == "__main__":
    processar_csv("sujo.csv", "limpo.csv")
