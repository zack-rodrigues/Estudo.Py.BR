leet_dict = {
    'A': '4', 'B': '8', 'C': '(', 'D': '|)', 'E': '3', 'F': '|=',
    'G': '6', 'H': '#', 'I': '1', 'J': '_|', 'K': '|<', 'L': '1',
    'M': '/\\/\\', 'N': '|\\|', 'O': '0', 'P': '|*', 'Q': '0_', 'R': '|2',
    'S': '5', 'T': '7', 'U': '|_|', 'V': '\\/', 'W': '\\/\\/', 'X': '><',
    'Y': '`/', 'Z': '2'
}

texto = input("Digite um texto para converter em leet speak: ")
leet = ''

for char in texto.upper():
    leet += leet_dict.get(char, char)  # Usa o símbolo se estiver no dicionário, senão mantém o caractere

print("\nTexto em leet speak:")
print(leet)
