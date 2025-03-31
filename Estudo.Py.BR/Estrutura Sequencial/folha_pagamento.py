ganho_por_hora=float(input('Quanto você ganha por horas trabalhadas: '))
horas_no_mes=float(input('Quanto você trabalhou no mês: '))

sal_bruto=float(ganho_por_hora*horas_no_mes)

inss=0.08
sindi=0.05
ir=0.11

desconto_inss=sal_bruto*inss
desconto_sindi=sal_bruto*sindi
desconto_ir=sal_bruto*ir

sal_liquid=sal_bruto -(desconto_inss + desconto_ir + desconto_sindi)

print(f'Seu salário bruto é: R${sal_bruto}')
print(f'O desconto do INSS foi: R${desconto_inss}')
print(f'O desconto do sindicato foi: R${desconto_sindi}')
print(f'O desconto do IR foi: R${desconto_ir}')
print(f'Seu Salário líquido é de: R${sal_liquid}')