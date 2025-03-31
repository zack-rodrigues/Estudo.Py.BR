dia=int(input('Insira um dia: '))
mes=int(input('Insira um mes: '))
ano=int(input('Insira um ano: '))

listdias=list(range(1,31))
listmeses=list(range(1,12))   # eu ia digitar um por um KKKK mas dai descobri
listanos=list(range(1,3000))  # essa função de list e range, ajudo 

if dia not in listdias:
    print('Insira uma data válida...')

elif mes not in listmeses:
    print('Insira uma data válida...')    

elif ano not in listanos:
    print('Insira uma data válida...')

else:
    print(f'Hoje é: {dia}/{mes}/{ano}')