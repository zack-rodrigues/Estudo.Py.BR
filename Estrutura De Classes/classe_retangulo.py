class Retangulo:
    def __init__(self,lado_a,lado_b):
        self.lado_a=lado_a
        self.lado_b=lado_b

    def retornar_lados(self):
        print(f'Os lados são: {self.lado_a} e {self.lado_b}')
    
    def mudar_lados(self,novo_lado_a,novo_lado_b):
        self.lado_a=novo_lado_a
        self.lado_b=novo_lado_b
        print(f'Os novos lados são: {self.lado_a} e {self.lado_b}')

    def calcular_area(self):
        area=self.lado_a*self.lado_b
        print(f'A area é: {area}')
        return area
    
    def calcular_perimetro(self):
        perimetro=(self.lado_a+self.lado_b)*2
        print(f'O perimetro é : {perimetro}')
        return perimetro


retangulo1=Retangulo(10,20)

retangulo1.retornar_lados()
retangulo1.calcular_area()
retangulo1.calcular_perimetro()
retangulo1.mudar_lados(5,10)
retangulo1.retornar_lados()
retangulo1.calcular_area()
retangulo1.calcular_perimetro()


        