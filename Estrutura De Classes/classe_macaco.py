class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if not self.bucho:
            return f"{self.nome} está com o bucho vazio."
        return f"{self.nome} tem no bucho: {', '.join(self.bucho)}."

    def digerir(self):
        if self.bucho:
            self.bucho.clear()
            return f"{self.nome} digeriu tudo o que estava no bucho."
        return f"{self.nome} não tem nada para digerir."


macaco2 = Macaco("Macaco2")
macaco1 = Macaco("Macaco1")

macaco1.comer("banana")
macaco1.comer("maçã")
print(macaco1.verBucho())

macaco2.comer("laranja")
macaco2.comer("uva")
print(macaco2.verBucho())


macaco1.comer("Macaco2")
print(macaco1.verBucho())

macaco1.digerir()
print(macaco1.verBucho())