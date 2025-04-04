def desenha_moldura(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    
    print("+" + "-" * (colunas - 2) + "+")
    for _ in range(linhas - 2):
        print("|" + " " * (colunas - 2) + "|")
    if linhas > 1:
        print("+" + "-" * (colunas - 2) + "+")


def main():
    linhas = int(input("Digite o número de linhas (1-20): "))
    colunas = int(input("Digite o número de colunas (1-20): "))
    desenha_moldura(linhas, colunas)

main()
