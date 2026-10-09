import csv
import re
from datetime import datetime

def limpar_nome(nome):
    return " ".join(nome.strip().split()).title()

def limpar_telefone(telefone):
    return re.sub(r"\D", "", telefone)

def limpar_data(data):
    try:
        dt = datetime.strptime(data.strip(), "%d/%m/%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return "inválido"

def criar_dataset_sujo(arquivo):
    linhas = [
        {"nome": "  joão   silva ", "telefone": "(48) 99999-1234 ", "data": "12/05/2024"},
        {"nome": "maria de souza", "telefone": "48988881234", "data": "01/01/2023"},
        {"nome": "CARLOS   ALMEIDA ", "telefone": "+55 48 91234-5678 ", "data": "31/12/2022"},
        {"nome": "ana   paula", "telefone": "123456789", "data": "15/08/2021"},
        {"nome": "Pedro   henrique ", "telefone": "48-99123-4567", "data": "07/07/2020"},
        {"nome": "lucas   ", "telefone": "(48)991234567", "data": "29/02/2019"},
    ]
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "telefone", "data"])
        writer.writeheader()
        writer.writerows(linhas)

def processar_csv(entrada, saida):
    with open(entrada, newline="", encoding="utf-8") as f_in, \
         open(saida, "w", newline="", encoding="utf-8") as f_out:
        
        reader = csv.DictReader(f_in)
        fieldnames = ["nome", "telefone", "data", "status"]
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            nome = limpar_nome(row["nome"])
            telefone = limpar_telefone(row["telefone"])
            data = limpar_data(row["data"])

            status = "válido"
            if len(telefone) != 11 or data == "inválido":
                status = "inválido"

            writer.writerow({
                "nome": nome,
                "telefone": telefone,
                "data": data,
                "status": status
            })

if __name__ == "__main__":
    criar_dataset_sujo("sujo.csv")
    processar_csv("sujo.csv", "limpo.csv")
    print("Arquivo limpo.csv gerado com sucesso!")

