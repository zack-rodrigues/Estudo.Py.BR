periodo=str(input('Qual periodo do dia você trabalha? \n M para matutino \n V para vespertino \n N para noturno \n Qual seu periodo? '))

if periodo == 'M' or periodo == 'm':
    print('Bom dia meu nobre')

elif periodo == 'V' or periodo == 'v':
    print('Boa tarde meu rei')

elif periodo == 'N' or periodo == 'n':
    print('Boa noite meu parça')

else:
    print('Valor Invalido amigão...')