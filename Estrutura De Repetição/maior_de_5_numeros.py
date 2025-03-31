numeros=[4,444,59,90,13]
maior=max(numeros)

for numero in numeros:
    if numero == maior:
        print(f'{numero} is the biggest')
        break
