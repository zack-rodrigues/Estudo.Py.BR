def imprimir_triangulo(n):
    for i in range(1, n + 1):
        print(' '.join(str(j) for j in range(1, i + 1)))

# Solicita um número ao usuário
n = int(input("Digite um número inteiro: "))
imprimir_triangulo(n)


# ou

def imprimir_triangulo(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Solicita um número ao usuário
n = int(input("Digite um número inteiro: "))
imprimir_triangulo(n)
