import random

def embaralha_palavra(palavra):
    return ''.join(random.sample(palavra, len(palavra))).lower()


def main():
    palavra = input("Digite uma palavra: ")
    print(f"Palavra embaralhada: {embaralha_palavra(palavra)}")


main()


#sem import

def embaralha_palavra(palavra):
    palavra = list(palavra.lower())
    tamanho = len(palavra)
    
    for i in range(tamanho - 1, 0, -1):
        j = i % tamanho  # Simulação simples de embaralhamento
        palavra[i], palavra[j] = palavra[j], palavra[i]
    
    return ''.join(palavra)


def main():
    palavra = input("Digite uma palavra: ")
    print(f"Palavra embaralhada: {embaralha_palavra(palavra)}")


main()

