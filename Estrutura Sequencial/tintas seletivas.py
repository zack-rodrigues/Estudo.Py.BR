metros_para_pintar = float(input('Quantos M2 deseja pintar: '))
litragem_lata = 18.00
preço_lata = 80.00
litragem_galão = 3.60
preço_galão = 25.00
m2porlata = 108.00  # Cobertura total de uma lata de 18 litros
m2porgalão = 21.60  # Cobertura total de um galão de 3,6 litros

# Função para arredondar para cima sem usar módulos
def arredondar_para_cima(valor):
    if valor % 1 == 0:
        return int(valor)
    else:
        return int(valor) + 1

# Calcular a quantidade necessária de latas e galões considerando 10% de folga
quantidade_de_latas_necessarias = metros_para_pintar / m2porlata * 1.1
quantidade_de_galões_necessários = metros_para_pintar / m2porgalão * 1.1

# Arredondar para cima
quantidade_de_latas = arredondar_para_cima(quantidade_de_latas_necessarias)
quantidade_de_galões = arredondar_para_cima(quantidade_de_galões_necessários)

# Calcular o custo total
custo_total_latas = quantidade_de_latas * preço_lata
custo_total_galões = quantidade_de_galões * preço_galão

# Verificar qual combinação (latas + galões) tem o menor desperdício
desperdicio_latas = quantidade_de_latas * m2porlata - metros_para_pintar
desperdicio_galões = quantidade_de_galões * m2porgalão - metros_para_pintar

if desperdicio_latas < desperdicio_galões:
    print(f'Melhor opção: {quantidade_de_latas} latas e 0 galões')
    print(f'Custo total: R${custo_total_latas:.2f}')
else:
    print(f'Melhor opção: 0 latas e {quantidade_de_galões} galões')
    print(f'Custo total: R${custo_total_galões:.2f}')
