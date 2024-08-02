kg_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
kg_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

if kg_morangos <= 5:
    valor_morangos = kg_morangos * preco_morango_ate_5kg
else:
    valor_morangos = (5 * preco_morango_ate_5kg) + ((kg_morangos - 5) * preco_morango_acima_5kg)

if kg_macas <= 5:
    valor_macas = kg_macas * preco_maca_ate_5kg
else:
    valor_macas = (5 * preco_maca_ate_5kg) + ((kg_macas - 5) * preco_maca_acima_5kg)

valor_total = valor_morangos + valor_macas

if kg_morangos + kg_macas > 8 or valor_total > 25:
    valor_total *= 0.90  

print(f"O valor a ser pago pelo cliente é R$ {valor_total:.2f}")
