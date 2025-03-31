altura=float(input('digite sua altura para encontrar o peso ideal: '))
alturaemmetros=float(altura/100)
peso_ideal_h=float((72.7*alturaemmetros)-58)
peso_ideal_m=float((62.1*alturaemmetros)-44.7)


print('Seu peso ideal como mulher é : ' ,peso_ideal_m)
print('Seu peso ideal como homem é : ' ,peso_ideal_h)
