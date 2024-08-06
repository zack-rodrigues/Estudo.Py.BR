nome = ''
while len(nome) <= 3:
    nome = input('Diga seu nome: ')
    if len(nome) <= 3:
        print('Nome deve ter mais de 3 caracteres.')

idade = -1
while not (0 <= idade <= 120):
    idade = int(input('Digite sua idade: '))
    if not (0 <= idade <= 120):
        print('Idade deve estar entre 0 e 120.')

salario = -1
while salario <= 0:
    salario = float(input('Digite seu salário: '))
    if salario <= 0:
        print('Salário deve ser maior que zero.')

sexo = ''
while sexo not in ('f', 'm'):
    sexo = input('Qual seu sexo? f ou m: ')
    if sexo not in ('f', 'm'):
        print('Sexo deve ser "f" ou "m".')

estados_civis = ('s', 'c', 'v', 'd')
civil = ''
while civil not in estados_civis:
    civil = input('Qual seu estado civil (s, c, v, d): ')
    if civil not in estados_civis:
        print('Estado civil deve ser "s", "c", "v" ou "d".')

print(f'Nome: {nome}\nIdade: {idade}\nSalário: {salario:.2f}\nSexo: {sexo}\nEstado Civil: {civil}')
