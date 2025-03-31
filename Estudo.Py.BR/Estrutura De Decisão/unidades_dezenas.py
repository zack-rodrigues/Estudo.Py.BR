numero = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7]

# Itera sobre cada número na lista
for num in numero:
    unidades = num % 10
    dezenas = (num // 10) % 10
    centenas = (num // 100) % 10
    
    # Pluraliza as palavras para cada número
    plural_centenas = 's' if centenas != 1 else ''
    plural_dezenas = 's' if dezenas != 1 else ''
    plural_unidades = 's' if unidades != 1 else ''
    
    # Exibe o resultado para o número atual
    print(f'Para o número {num}: {centenas} centena{plural_centenas}, {dezenas} dezena{plural_dezenas}, {unidades} unidade{plural_unidades}.')
