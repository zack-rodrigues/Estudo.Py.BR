class Quadrado:
    def __init__(self,tamanho_lado):
        self.tamanho_lado=tamanho_lado
    
    def mudar_lado(self,novo_lado):
        self.tamanho_lado=novo_lado
        print(f'novo tamanho de lado é {self.tamanho_lado}')
    
    def retornar_lado(self):
         print(f'Atualmente o tamnho do lado é: {self.tamanho_lado}')

    def calcular_area(self):
           area=self.tamanho_lado**2
           print(f'A area é de {area}')


quadrado1=Quadrado(10)

quadrado1.retornar_lado()
quadrado1.calcular_area()
quadrado1.mudar_lado(5)
quadrado1.calcular_area()
quadrado1.retornar_lado()
        
