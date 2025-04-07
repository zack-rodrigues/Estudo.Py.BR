class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material
    
    def trocarcor(self,nova_cor):
        self.cor=nova_cor
        print(f'A cor da bola agora é {self.cor}')
        
    def mostrarcor(self):
        print(f'A cor da bola é {self.cor}')

bola1=Bola('azul','30cm','couro')

bola1.mostrarcor()
bola1.trocarcor('pink')

