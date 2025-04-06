frase=str(input('Digite uma frase: '))
frase2=str(input('Digite outra frase: '))

print(f'A primeira frase, {frase} contém {len(frase)} caracteres.')
print(f'A segunda frase, {frase2} contém {len(frase2)} caracteres.')

if len(frase) == len(frase2):
    print('As frases tem a mesma quantidade de caracteres.')
else:
    print('As frases tem quantidades de caracteres diferentes.')

if frase == frase2:
    print('As frases são iguais.')
else:
    print('As frases são diferentes.')




