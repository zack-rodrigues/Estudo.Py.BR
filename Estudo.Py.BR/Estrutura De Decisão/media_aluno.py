nota1=float(input('Digite sua nota mensal:'))
nota2=float(input('Digite sua nota bimestral:'))

media_mensal=(nota1+nota2)/2

if media_mensal >= 6 and media_mensal < 10:
    print(f'Parabéns sua média é:  {media_mensal} e você passou!')

elif media_mensal == 10:
    print(f'Wow ... média {media_mensal}!!!')

else:
    print(f'Poxa você não passou, sua média foi..: {media_mensal}')
