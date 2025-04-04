from itertools import permutations

def verifica_quadrado_magico(matriz):
    soma = sum(matriz[0])
    return (
        all(sum(linha) == soma for linha in matriz) and
        all(sum(matriz[i][j] for i in range(3)) == soma for j in range(3)) and
        sum(matriz[i][i] for i in range(3)) == soma and
        sum(matriz[i][2 - i] for i in range(3)) == soma
    )


def gera_quadrados_magicos():
    quadrados_magicos = []
    for perm in permutations(range(1, 10)):
        matriz = [list(perm[i:i + 3]) for i in range(0, 9, 3)]
        if verifica_quadrado_magico(matriz):
            quadrados_magicos.append(matriz)
    return quadrados_magicos


def exibir_quadrados(quadrados):
    for idx, quadrado in enumerate(quadrados, 1):
        print(f"\nQuadrado Mágico {idx}:")
        for linha in quadrado:
            print(" ".join(map(str, linha)))


def main():
    quadrados = gera_quadrados_magicos()
    exibir_quadrados(quadrados)
    print(f"\nTotal de quadrados mágicos encontrados: {len(quadrados)}")


main()


#sem import

def verifica_quadrado_magico(matriz):
    """Verifica se a matriz 3x3 é um quadrado mágico."""
    soma = sum(matriz[0])
    return (
        all(sum(linha) == soma for linha in matriz) and
        all(sum(matriz[i][j] for i in range(3)) == soma for j in range(3)) and
        sum(matriz[i][i] for i in range(3)) == soma and
        sum(matriz[i][2 - i] for i in range(3)) == soma
    )


def gera_permutacoes(lista):
    """Gera todas as permutações possíveis de uma lista sem usar import."""
    if len(lista) == 1:
        return [lista]
    permutacoes = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]
        for p in gera_permutacoes(resto):
            permutacoes.append([lista[i]] + p)
    return permutacoes


def gera_quadrados_magicos():
    """Gera todos os quadrados mágicos possíveis com os números de 1 a 9."""
    quadrados_magicos = []
    for perm in gera_permutacoes(list(range(1, 10))):
        matriz = [perm[i:i + 3] for i in range(0, 9, 3)]
        if verifica_quadrado_magico(matriz):
            quadrados_magicos.append(matriz)
    return quadrados_magicos


def exibir_quadrados(quadrados):
    """Exibe todos os quadrados mágicos encontrados."""
    for idx, quadrado in enumerate(quadrados, 1):
        print(f"\nQuadrado Mágico {idx}:")
        for linha in quadrado:
            print(" ".join(map(str, linha)))


def main():
    quadrados = gera_quadrados_magicos()
    exibir_quadrados(quadrados)
    print(f"\nTotal de quadrados mágicos encontrados: {len(quadrados)}")


main()
