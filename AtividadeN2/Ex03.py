import sys

numeros = [3, 7, 2, 8, 4, 10, 5]

menor = sys.maxsize

for n in numeros:
    if n < menor:
        menor = n
print(menor)
