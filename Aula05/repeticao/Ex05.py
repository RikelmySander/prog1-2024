<<<<<<< HEAD
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
=======
"""
Exercício 05 – Crie um programa que solicita ao usuário para inserir números positivos
e calcula a média desses números, ignorando números negativos e zeros.
Calcule a média quando o usuário pressionar 0.

Entrada:
Digite um número positivo (ou 0 para sair): 5
Digite um número positivo (ou 0 para sair): 4
Digite um número positivo (ou 0 para sair): 1
Digite um número positivo (ou 0 para sair): 0

Saída:
A média dos números positivos é: 3.333333
"""
>>>>>>> a25262c6ad3fc0deef8a1c0eb5b653a0323c0944
