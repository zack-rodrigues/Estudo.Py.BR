
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print('Qual operação deseja realizar? Escolha uma abaixo e digite:')
escolha = int(input('1 - Para saber se é par ou ímpar\n2 - Para saber se é positivo ou negativo\n3 - Para saber se é inteiro ou decimal\n'))

if escolha == 1:
    
    if num1 % 2 == 0:
        print(f'O primeiro número é par.')
    else:
        print(f'O primeiro número é ímpar.')
    
    if num2 % 2 == 0:
        print(f'O segundo número é par.')
    else:
        print(f'O segundo número é ímpar.')

elif escolha == 2:

    if num1 > 0:
        print(f'O primeiro número é positivo.')
    elif num1 < 0:
        print(f'O primeiro número é negativo.')
    else:
        print(f'O primeiro número é zero.')

    if num2 > 0:
        print(f'O segundo número é positivo.')
    elif num2 < 0:
        print(f'O segundo número é negativo.')
    else:
        print(f'O segundo número é zero.')

elif escolha == 3:

    if num1.is_integer():
        print(f'O primeiro número é inteiro.')
    else:
        print(f'O primeiro número é decimal.')

    if num2.is_integer():
        print(f'O segundo número é inteiro.')
    else:
        print(f'O segundo número é decimal.')

else:
    print('Escolha inválida.')
