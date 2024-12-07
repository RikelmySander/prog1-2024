emails = [
    "joao@google.com",
    "maria@apple.com",
    "carlos@microsoft.com",
    "ana@google.com",
    "paulo@amazon.com",
    "lucas@apple.com"
]
dominios = []

for e in emails:
    email_sep = e.split("@")
    dominio = email_sep[1]
    if dominio not in dominios:
        dominios.append(dominio)

print(dominios)
