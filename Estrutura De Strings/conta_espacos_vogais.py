frase=(input('digite uma frase: '))
vogais = ['a', 'e', 'i', 'o', 'u']
contagemvogal=0
contagemespaco=0

for i in frase:
    if i == ' ':
        contagemespaco+=1
    elif i in vogais:
        contagemvogal+=1


print(f'A frase tem, {contagemespaco} espaços e {contagemvogal} vogais.')

