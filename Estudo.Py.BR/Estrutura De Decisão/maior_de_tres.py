num1=float(input('Digite um número...'))
num2=float(input('Digite um segundo número...'))
num3=float(input('Digite um terceiro número...'))

if num1 > num2 and num1 > num3:
    print(f'Número {num1} é o maior dos tres...')

elif num2 > num1 and num2 > num3:
    print(f'Número {num2} é o maior dos tres...')

else:
    print(f'Número {num3} é o maior dos tres...')
