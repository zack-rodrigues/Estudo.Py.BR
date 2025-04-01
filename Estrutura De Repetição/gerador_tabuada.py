while True:
    try:
        tabuada=int(input('Digite um número para gerar sua tabuada:'))
        break
    except ValueError:
        print('Apenas números inteiros.')

multiplicando=range(1,11)

for numero in multiplicando:
    resultado=numero*tabuada
    print(f'{tabuada}X{numero}={resultado}')
