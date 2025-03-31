while True:
 nota = input('Digite uma nota: ')
    
 if nota.isdigit() and int(nota) in range(1, 11):  
  print('Sua nota é', int(nota))
  break  
 else:
  print('Valor entre 1 e 10 apenas')