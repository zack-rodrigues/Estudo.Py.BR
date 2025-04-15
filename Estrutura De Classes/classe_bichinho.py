class Tamagushi:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = max(0, min(100, nova_fome))  

    def alterarSaude(self, nova_saude):
        self.saude = max(0, min(100, nova_saude))  

    def alterarIdade(self, nova_idade):
        self.idade = max(0, nova_idade)  

    def retornarHumor(self):
        
        if self.fome < 30 and self.saude > 70:
            return "Feliz"
        elif self.fome > 70 or self.saude < 30:
            return "Triste"
        else:
            return "Neutro"