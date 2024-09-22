total = 0
n_digitador = 0
while True:
    n1 = float(input("Digite um numero positivo:(ou 0 para sair)"))
    if n1 == 0 :
        break
    if n1 < 0:
        continue
    if n1 > 0:
        total = total + n1
        n_digitador += 1
print(total/n_digitador)