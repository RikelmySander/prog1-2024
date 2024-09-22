"""
Exercício 03 – Peça ao usuário três números inteiros
e exiba qual é o maior e qual é o menor entre eles.
Defina as funções: encontrar_maior e encontrar_menor.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8

Saída:
O maior número é 10.
O menor número é 5.
"""
def find_the_biggest(n1, n2, n3):
    if n1>n2 and n1>n3:
        #result = print(f"The biggest number is {n1}")
        #Or 
        return n1
    elif n2>n1 and n2>n3:
        #print(f"The biggest number is {n2}")
        #Or 
        return n2
    else:
        #print(f"The biggest number is {n3}")
        #Or 
        return n3

def find_the_smaller(n1, n2, n3):
    if n1<n2 and n1<n3:
        #print(f"the smaller number is {n1}")
        #Or 
        return n1
    elif n2<n1 and n2<n3:
        #result = print(f"the smaller number is {n2}")
        #Or 
        return n2
    else:
        #result = print(f"the smaller number is {n3}")
        #Or 
        return n3
    
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Encontrando o maior e o menor número
bigger = {find_the_biggest(number1, number2, number3)}
smaller = {find_the_smaller(number1, number2, number3)}

# Exibindo o resultado
print(f"The biggest number is {bigger}.")
print(f"the smaller number is {smaller}.")
