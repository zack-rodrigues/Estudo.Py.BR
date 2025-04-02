idades = []
alturas = []

for indice in range(5):
    idade = int(input(f"Digite a idade da pessoa {indice + 1}: "))
    altura = float(input(f"Digite a altura da pessoa {indice + 1} (em metros): "))
    
    idades.append(idade)
    alturas.append(altura)

print("\nDados na ordem inversa:")
for indice in range(4, -1, -1):
    print(f"Pessoa {indice + 1}: Idade = {idades[indice]}, Altura = {alturas[indice]} metros")
