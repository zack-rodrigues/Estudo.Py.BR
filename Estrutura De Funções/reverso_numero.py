def reverso_numero(numero):
    """Retorna o reverso de um número inteiro."""
    return int(str(abs(numero))[::-1]) * (-1 if numero < 0 else 1)


def main():
    numero = int(input("Digite um número inteiro: "))
    print(f"O reverso de {numero} é {reverso_numero(numero)}")

main()
