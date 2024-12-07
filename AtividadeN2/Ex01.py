unicos = []

lista = [4, 7, 2, 7, 4, 8, 2, 9]

for n in lista:
    achou = False

    for u in unicos:
        if u == n:
            achou = True
            break
    if achou == False:
        unicos.append(n)

print(unicos)