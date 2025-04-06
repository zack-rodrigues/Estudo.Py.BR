unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dezenas = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
especiais = {
    11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
    16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove'
}

# Entrada
num = int(input("Digite um número entre 0 e 99: "))

# Validação
if 0 <= num <= 99:
    if 0 <= num <= 9:
        print(unidades[num])
    elif num == 10:
        print('dez')
    elif 11 <= num <= 19:
        print(especiais[num])
    elif num % 10 == 0:
        print(dezenas[num // 10])
    else:
        dezena = dezenas[num // 10]
        unidade = unidades[num % 10]
        print(f'{dezena} e {unidade}')
else:
    print("Número fora do intervalo permitido.")
