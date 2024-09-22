"""
Exercício 01 – Crie um programa que solicita um número inteiro para o usuário.
Após isso, verifique se o número é par ou ímpar.
Crie uma função chamada eh_par que recebe um número inteiro e retorna True se o número for par e False se for ímpar.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número ímpar.
"""
num = int(input("Write a number: "))

def even_Number(number):
    return number % 2 == 0

if even_Number(num):
    print(f"this number {num} is even. this is function return {even_Number(num)}")
else:
    print(f"This number {num} is odd. This is function return {even_Number(num)}")