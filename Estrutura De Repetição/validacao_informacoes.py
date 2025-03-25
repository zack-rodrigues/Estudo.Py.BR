nome = ''
while len(nome) <= 3:
    nome = input("Digite seu nome (mais de 3 caracteres): ")

idade = -1
while idade < 0 or idade > 150:
    idade = int(input("Digite sua idade (0-150): "))

salario = -1
while salario <= 0:
    salario = float(input("Digite seu salário (maior que 0): "))

sexo = ''
while sexo not in ['f', 'm']:
    sexo = input("Digite seu sexo ('f' ou 'm'): ").lower()

estado_civil = ''
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ").lower()

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
