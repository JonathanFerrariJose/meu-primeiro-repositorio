import re

telefones = [
    "(48) 99999-1234",
    "48 98888 5678",
    "48-97777-0000",
    "48966661234",
    "fone: 48 95555-4321"
]

for tel in telefones:
    apenas_digitos = re.sub(r"\D", "", tel)

    if re.fullmatch(r"\d{11}", apenas_digitos):
        status = "válido"
    else:
        status = "inválido"
    
    print(f"{tel} -> {apenas_digitos} ({status})")
