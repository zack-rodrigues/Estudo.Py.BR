tamanho_arquivo_mb = float(input('Qual tamanho do seu arquivo em MB?: '))
velocidade_net_mbps = float(input('Qual a velocidade da sua internet em Mbps?: '))

# Converter Mbps para MB por segundo
velocidade_mb_por_segundo = velocidade_net_mbps / 8

# Calcular o tempo de download em segundos
tempo_segundos = tamanho_arquivo_mb / velocidade_mb_por_segundo

# Calcular minutos e segundos arredondados
minutos = int(tempo_segundos // 60)  # Parte inteira dos minutos
segundos = round(tempo_segundos % 60)  # Arredonda os segundos

# Se os segundos forem 60 após arredondamento, ajustar para um minuto
if segundos == 60:
    minutos += 1
    segundos = 0

# Exibir o resultado
if minutos == 1:
    print(f'Para baixar esse arquivo você vai levar: {minutos} minuto e {segundos} segundos.')
else:
    print(f'Para baixar esse arquivo você vai levar: {minutos} minutos e {segundos} segundos.')
