class Televisor:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:  
            self.canal = novo_canal
        else:
            print("Canal inválido. Escolha um canal entre 1 e 100.")

    def aumentar_volume(self):
        if self.volume < 100:  
            self.volume += 1
        else:
            print("Volume já está no máximo.")

    def diminuir_volume(self):
        if self.volume > 0:  
            self.volume -= 1
        else:
            print("Volume já está no mínimo.")

    def __str__(self):
        return f"Canal: {self.canal}, Volume: {self.volume}"

tv = Televisor()
print(tv)
tv.mudar_canal(5)
print(tv)
tv.aumentar_volume()
print(tv)
tv.diminuir_volume()
print(tv)