class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura

    def envelhecer(self,nova_idade_up):
        self.idade=self.idade+nova_idade_up
        print(f'A nova idade é {self.idade}')
    
    def engordar(self,novo_peso_up):
        self.peso=self.peso+novo_peso_up
        print(f'O novo peso é {self.peso}')

    def emagrecer(self,novo_peso_down):
        self.peso=self.peso-novo_peso_down
        print(f'O novo peso é {self.peso}')
    
    def crescer(self,crescimento_up):
        self.altura=self.altura+crescimento_up
        print(f'A nova altura é {self.altura}cm')

pessoa1=Pessoa('Zack',24,70,175)

pessoa1.envelhecer(10)
pessoa1.engordar(5)
pessoa1.emagrecer(2)
pessoa1.crescer(10)

    