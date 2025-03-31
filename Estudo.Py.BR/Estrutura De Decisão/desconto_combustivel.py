# desconto_combustivel.py

# Preços por litro
preco_alcool = 1.90
preco_gasolina = 2.50

# Definindo os descontos
desconto_alcool_ate_20 = 0.03
desconto_alcool_acima_20 = 0.05
desconto_gasolina_ate_20 = 0.04
desconto_gasolina_acima_20 = 0.06

# Entrada de dados
litros = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

# Verifica o tipo de combustível e aplica o desconto apropriado
if tipo_combustivel == 'A':  # Álcool
    preco_litro = preco_alcool
    if litros <= 20:
        desconto = desconto_alcool_ate_20
    else:
        desconto = desconto_alcool_acima_20

elif tipo_combustivel == 'G':  # Gasolina
    preco_litro = preco_gasolina
    if litros <= 20:
        desconto = desconto_gasolina_ate_20
    else:
        desconto = desconto_gasolina_acima_20

else:
    print("Tipo de combustível inválido. Use 'A' para álcool ou 'G' para gasolina.")
    exit()

# Calcula o valor total sem desconto
valor_total = litros * preco_litro

# Aplica o desconto
valor_com_desconto = valor_total * (1 - desconto)

# Imprime o resultado
print(f"O valor a ser pago é: R$ {valor_com_desconto:.2f}")
