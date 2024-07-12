produto1=float(input('Digite o preço de um produto: '))
produto2=float(input('Digite o preço do segundo produto: '))
produto3=float(input('Digite o preço do terceiro produto: '))

if produto1 < produto2 and produto1 < produto3:
    barato=produto1

elif produto2 < produto1 and produto2 < produto3:
    barato=produto2

else:
    barato=produto3

print(f' O valor do produto mais barato é {barato}')