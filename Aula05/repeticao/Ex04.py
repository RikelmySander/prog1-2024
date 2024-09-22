"""
Exercício 04 – Crie um programa que solicita ao usuário
para inserir uma série de números, e ele só irá somar
os números pares fornecidos. Use o comando continue.

Entrada:
Digite um número (ou 0 para sair): 5
Digite um número (ou 0 para sair): 4
Digite um número (ou 0 para sair): 1
Apenas números pares são somados. Tente novamente.
Digite um número (ou 0 para sair): 0

Saída:
A soma total dos números pares é: 4
"""
total_soma_pares = 0

while True:
    n1 = int(input("digite um numero:(ou 0 para sair) "))
    if n1 == 0:
        break
    if n1 % 2 != 0:
        print("Apenas numeros pares são somados")
        continue
    total_soma_pares = total_soma_pares + n1
print(f"A soma total dos pares é {total_soma_pares}")
    


