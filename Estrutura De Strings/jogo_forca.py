import random

# Lê palavras de um arquivo e escolhe uma aleatoriamente
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip().upper() for linha in arquivo if linha.strip()]

palavra_secreta = random.choice(palavras)
letras_descobertas = ['_' for _ in palavra_secreta]
tentativas = 0
letras_erradas = []

print("=== JOGO DA FORCA ===")
print(f"A palavra tem {len(palavra_secreta)} letras.")

while tentativas < 6 and '_' in letras_descobertas:
    print("\nPalavra:", ' '.join(letras_descobertas))
    letra = input("Digite uma letra: ").strip().upper()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_descobertas or letra in letras_erradas:
        print("Você já tentou essa letra.")
        continue

    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                letras_descobertas[i] = letra
    else:
        tentativas += 1
        letras_erradas.append(letra)
        print(f"-> Você errou pela {tentativas}ª vez. Tente de novo!")

if '_' not in letras_descobertas:
    print("\nParabéns! Você descobriu a palavra:", palavra_secreta)
else:
    print("\nVocê foi enforcado! A palavra era:", palavra_secreta)
