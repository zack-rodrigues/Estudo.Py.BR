def converte_hora(hora, minuto):
    if hora == 0:
        return 12, minuto, 'AM'
    elif hora == 12:
        return 12, minuto, 'PM'
    elif hora > 12:
        return hora - 12, minuto, 'PM'
    else:
        return hora, minuto, 'AM'

def exibe_hora(hora, minuto):
    hora_12, minuto, periodo = converte_hora(hora, minuto)
    print(f'A hora convertida é: {hora_12}:{minuto:02d} {periodo}')

hora_24 = int(input('Digite a hora (0-23): '))
minuto = int(input('Digite os minutos (0-59): '))

exibe_hora(hora_24, minuto)


