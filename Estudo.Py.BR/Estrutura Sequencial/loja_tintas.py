#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area=float(input('Quantos M2 tem a área que deseja pintar: '))
preço=80.00
volume=18

litros=(area/3)
quantidade_de_latas=litros/18

preço_total=quantidade_de_latas*preço


print(f'Você precisa comprar:{quantidade_de_latas:.2f} Latas de tinta !!')
print(f'Você precisa gastar:{preço_total:.2f} reais...')