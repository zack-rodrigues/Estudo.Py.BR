numeros_int=list(range(1,21))
pares=[]
impares=[]

for num in numeros_int:
    if num%2 == 0:
        pares.append(num)
    
    else:
        impares.append(num)

print(pares)
print(impares)
print(numeros_int)

