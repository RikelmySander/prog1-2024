senhas = ["senha123", "P@ssw0rd2024", "admin", "senha123!", "senhamuitomaiordoquedeveria"]


def possuiCaracterEspecialv1(senha: str):
    lista_caracteres = list(senha)
    for c in lista_caracteres:
        if c.isalnum() == False:
            return True
    return False
def possuiCaracterEspecialv2(senha: str):
    lista_caracteres = list(senha)
    possui_caracter_especial = False
    for c in lista_caracteres:
        if not c.isalnum():
            possui_caracter_especial = True
            break
    return possui_caracter_especial

for senha in senhas:
    if len(senha) < 8:
        print(f"{senha} - Senha Fraca")
    elif len(senha) >= 8 and len(senha) <= 12 and not possuiCaracterEspecialv2(senha):
        print(f"{senha} - Senha Média")
    elif len(senha) >= 8 and len(senha) <= 12 and possuiCaracterEspecialv2(senha):
        print(f"{senha} - Senha Forte")
    else:
        print(f"Senha fora dos requisitos: {senha}")

