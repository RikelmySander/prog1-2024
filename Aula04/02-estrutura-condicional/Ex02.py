"""
Exercício 02 – Peça ao usuário dois números inteiros e exiba as comparações:
maior, menor, igual.

Crie as funções: eh_menor, eh_igual.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5

Saída:
10 é maior que 5.
10 não é menor que 5.
10 não é igual a 5.
"""
def is_higher(a, b):
    return a > b

def is_smaller(a, b):
    return a < b

def is_the_same(a, b):
    return a == b

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Exibindo o resultado
if is_higher(number1, number2):
    print(f"{number1} is greater than {number2}.")
else:
    print(f"{number1} not is greater than {number2}.")

if is_smaller(number1, number2):
    print(f"{number1} is smaller than {number2}")
else:
    print(f"{number1} not is smaller than {number2}")

if is_the_same(number1, number2):
    print(f"{number1} is the same than {number2}")
else:
    print(f"{number1} not is the same than {number2}")