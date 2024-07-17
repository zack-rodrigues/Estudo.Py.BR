dia=int(input('Digite um dia para saber o dia da semana correspondente:'))
pool=[1,2,3,4,5,6,7]
dia_da_semana=0


if dia == 1:
    dia_da_semana='segunda'

elif dia == 2:
    dia_da_semana='terça'    
    
elif dia == 3:
    dia_da_semana='quarta' 

elif dia == 4:
    dia_da_semana='quinta'  

elif dia == 5:
    dia_da_semana='sexta'  

elif dia == 6:
    dia_da_semana='sabado'  

elif dia == 7:
    dia_da_semana='domingo'


if dia in pool:
 print (f'O dia da semana correspondente a {dia}, é {dia_da_semana}')

else:
    print('Valor Inválido')
   