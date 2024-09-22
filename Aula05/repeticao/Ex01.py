"""
Exercício 01 - Crie um programa que solicite ao usuário um número inteiro positivo
e, em seguida, faça uma contagem regressiva desse número até 1.

Entrada:
Digite um número inteiro positivo: 5

Saída:
5
4
3
2
1
Contagem regressiva concluída.
"""
import time 
numero = int(input("Digite um número inteiro positivo: "))
for n in range(numero,0,-1):
    time.sleep(1)
    print(n)
