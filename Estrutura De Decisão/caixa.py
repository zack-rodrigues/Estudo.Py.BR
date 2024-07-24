saque = int(input('Quanto deseja sacar? R$'))

if saque < 10 or saque > 600:
    print("Valor de saque não permitido. O valor mínimo é R$10 e o máximo é R$600.")
else:
    notas_de_100 = saque // 100
    saque %= 100
    
    notas_de_50 = saque // 50
    saque %= 50
    
    notas_de_10 = saque // 10
    saque %= 10
    
    notas_de_5 = saque // 5
    saque %= 5
    
    notas_de_1 = saque
    
    print(f"Notas fornecidas:")
    if notas_de_100 > 0:
        print(f"{notas_de_100} nota(s) de R$100")
    if notas_de_50 > 0:
        print(f"{notas_de_50} nota(s) de R$50")
    if notas_de_10 > 0:
        print(f"{notas_de_10} nota(s) de R$10")
    if notas_de_5 > 0:
        print(f"{notas_de_5} nota(s) de R$5")
    if notas_de_1 > 0:
        print(f"{notas_de_1} nota(s) de R$1")
