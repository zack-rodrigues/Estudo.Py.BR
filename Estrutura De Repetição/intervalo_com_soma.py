# Recebe dois números inteiros do usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma=0

# Garante que o primeiro número seja sempre o menor
if numero1 > numero2:
    numero1, numero2 = numero2, numero1  # Troca os valores, se necessário

# Gera inteiros no intervalo
for numero in range(numero1 + 1, numero2):
    soma+=numero #vai somando a cada vez que o loop passa em cada um


print(soma) #mostra a soma
