import sys

numeros = [3, 7, 2, 8, 4, 10, 5]

maior = -sys.maxsize

for n in numeros:
    if n > maior:
        maior = n
print(maior)
