# Recebe dois números inteiros do usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Garante que o primeiro número seja sempre o menor
if numero1 > numero2:
    numero1, numero2 = numero2, numero1  # Troca os valores, se necessário

# Gera e imprime os números inteiros no intervalo
for numero in range(numero1 + 1, numero2):
    print(numero)
