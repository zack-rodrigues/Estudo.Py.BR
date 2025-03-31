#Faça um Programa que peça um número e informe se o número é
#inteiro ou decimal. Dica: utilize uma função de arredondamento.
try:
 numero=float(input('Informe um número para saber se ele é inteiro ou decimal: '))

 if numero.is_integer():
    print('inteiro')

 else:
    print('Decimal')


except ValueError:
  print('Coé, só numeros po')


