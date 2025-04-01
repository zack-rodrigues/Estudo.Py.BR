caracteres=list('abcdefghij')
contador=0
vogais=list('aeiou')

for consoantes in caracteres:
    if consoantes in vogais:
        continue
    else:
        contador+=1
        
        print(consoantes, end='')

print('\nquantidade de consoantes é:',contador)