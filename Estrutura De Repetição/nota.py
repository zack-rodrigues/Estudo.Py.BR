intervalo_validos = range(0, 11)

while True:
    # Solicita ao usuário que digite a nota
    nota = int(input('Digite sua nota de 0 a 10: '))

    # Verifica se a nota está no intervalo válido usando um for loop
    for valor in intervalo_validos:
        if nota == valor:
            print('Sua nota foi registrada.')
            break
    else:
        print('Nota inválida. Tente novamente.')
        continue  # Volta ao início do loop para pedir a nota novamente
      # Sai do loop se a nota for válida
    break
