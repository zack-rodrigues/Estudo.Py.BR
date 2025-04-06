import random

# Lê as palavras do arquivo
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]

# Escolhe e embaralha uma palavra
palavra_original = random.choice(palavras)
letras = list(palavra_original)
random.shuffle(letras)
palavra_embaralhada = ''.join(letras)

print("=== JOGO DA PALAVRA EMBARALHADA ===")
print(f"Adivinhe a palavra: {palavra_embaralhada}")
tentativas = 6

# Tentativas do jogador
while tentativas > 0:
    tentativa = input("Qual é a palavra? ").strip().lower()
    if tentativa == palavra_original:
        print("Parabéns! Você acertou! 🎉")
        break
    else:
        tentativas -= 1
        print(f"Errado! Você ainda tem {tentativas} tentativa(s).")

if tentativas == 0:
    print(f"Que pena! Você perdeu. A palavra era: {palavra_original}")
