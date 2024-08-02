notas = list(range(0, 11))

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    
    if nota not in notas:
        print("Nota inválida. Digite um valor entre 0 e 10.")
    else:
        break
print('Nota registrada')