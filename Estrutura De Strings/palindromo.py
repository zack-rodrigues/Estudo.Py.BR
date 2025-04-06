import string

frase = input("Digite uma frase: ")

print(f"\nFrase original: {frase}")

frase_limpa = ''.join(
    letra.lower() for letra in frase if letra.isalnum()
)

if frase_limpa == frase_limpa[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
