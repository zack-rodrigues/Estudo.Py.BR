salario=float(input('Qual seu salário atual? R$'))

if salario <= 280.00:
   aumento_total=salario*1.20
   porcentagem=1.20

elif salario <= 700 and salario > 280:
     aumento_total=salario*1.15
     porcentagem=1.15

elif salario <= 1500 and salario > 700:
     aumento_total=salario*1.10
     porcentagem=1.10

elif salario > 1500:
     aumento_total=salario*1.05
     porcentagem=1.05

aumento=aumento_total-salario
trueporcentagem=(porcentagem-1)*100

print(f'Seu salário anterior era de R${salario:.2f}')
print(f'A porcentagem de aumento vai ser {trueporcentagem:.2f}%')
print(f'O valor do aumento sera de R${aumento:.2f}')
print(f'Logo o seu salario vai para R${aumento_total:.2f}')

  