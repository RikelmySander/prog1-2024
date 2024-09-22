"""
Exercício 06 - Crie um programa onde o usuário deve adivinhar
um número gerado aleatoriamente entre 1 a 100. A cada tentativa,
exiba se ele deve tentar um número maior ou menor.
Quando o número for acertado, exiba o número de tentativas.
Dica: para gerar o número aleatório, utilize o seguinte código:
import random
numero_secreto = random.randint(1, 100)

Exemplo:
Digite um número: 50
Tente um número maior.
Digite um número: 80
Tente um número menor.
Digite um número: 61
Parabéns! Você acertou o número em 3 tentativas.
"""
import random
n_secret = random.randint(1,100)
tentativas = 0
while True:
    n_do_ususario = int(input("Digite um numero: "))
    tentativas += 1
    if n_do_ususario > n_secret:
        print("Digite um numero menor!")
    elif n_do_ususario < n_secret:
        print("Digite um numero maior!")
        continue
    else:
        print(f"Voce acertou, em {tentativas} tentativas!!")