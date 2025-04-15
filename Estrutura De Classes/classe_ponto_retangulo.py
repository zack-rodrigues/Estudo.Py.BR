class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Retangulo:
    def __init__(self, largura=0, altura=0, origem=None):
        self.largura = largura
        self.altura = altura
        self.origem = origem if origem else Ponto()

    def imprimir_ponto(self):
        print(f"Ponto de origem: {self.origem}")

    def encontrar_centro(self):
        centro_x = self.origem.x + self.largura / 2
        centro_y = self.origem.y + self.altura / 2
        return Ponto(centro_x, centro_y)


def menu():
    retangulo = Retangulo()
    while True:
        print("\nMenu:")
        print("1. Alterar retângulo")
        print("2. Imprimir ponto de origem")
        print("3. Imprimir centro do retângulo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            largura = float(input("Digite a largura do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            x = float(input("Digite a coordenada x do ponto de origem: "))
            y = float(input("Digite a coordenada y do ponto de origem: "))
            retangulo = Retangulo(largura, altura, Ponto(x, y))
        elif opcao == "2":
            retangulo.imprimir_ponto()
        elif opcao == "3":
            centro = retangulo.encontrar_centro()
            print(f"Centro do retângulo: {centro}")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()