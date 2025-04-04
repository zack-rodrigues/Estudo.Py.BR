def quantidade_digitos(numero):
    return len(str(abs(numero)))


def main():
    numero = int(input("Digite um número inteiro: "))
    qtd = quantidade_digitos(numero)
    print(f"O número {numero} tem {qtd} dígito(s).")


main()
