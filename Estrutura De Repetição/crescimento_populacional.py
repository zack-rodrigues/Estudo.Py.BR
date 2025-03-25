pais_a=80000
pais_b=200000
anos=0

while True:
    if pais_a >= pais_b:
     print(f'Ultrapassou em {anos} anos.')
     break
    else:
     pais_a+=pais_a*0.030
     pais_b+=pais_b*0.015
     anos+=1


#exemplo em for

pais_a = 80000
pais_b = 200000
anos = 0

for anos in range(1, 1000):  
    pais_a += pais_a * 0.030 
    pais_b += pais_b * 0.015  
    
    if pais_a >= pais_b:
        print(f'Ultrapassou em {anos} anos.')
        break


