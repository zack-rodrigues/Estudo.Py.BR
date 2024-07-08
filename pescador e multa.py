limite=50
multa=4
peso_de_peixes=float(input('Insira a quantidade de peixes que obteve hoje em KG, para verificarmos..: '))

if peso_de_peixes > limite:
   excesso=peso_de_peixes-limite
   print(' Opa! passou de 50kg.. pague R$' , excesso*multa, 'de multa :(' )


else:
 print('Tudo Certo! não pague multa...')