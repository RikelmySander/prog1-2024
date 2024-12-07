"""
Escreva um programa em Python que receba um texto e uma palavra. Conte quantas vezes cada palavra
aparece no texto.
"""

texto = "O Python é ótimo. Eu amo Python porque Python é fácil de aprender."
palavras = texto.replace(".","").split(" ")
impressos = []

for p in palavras:
    if p not in impressos:
        ocorrencias = palavras.count(p)
        impressos.append(p)
        print(f"{p} - {ocorrencias} palvaras")
