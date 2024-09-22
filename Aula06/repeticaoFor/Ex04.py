"""
Desenvolva um programa que faz uma contagem regressiva,
imprimindo os números de 20 até 1.
"""
import time 
i = 20 
while True:
    if i >= 0:
        time.sleep(1)
        print(i)
        i -=1
        continue
    else:
        break
