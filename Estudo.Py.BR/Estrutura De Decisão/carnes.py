tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra, Picanha): ")
quantidade_kg = float(input("Digite a quantidade de carne (em Kg): "))
pagamento = input("Digite o tipo de pagamento (dinheiro ou cartão): ")

if tipo_carne == "File Duplo":
    preco_ate_5kg = 4.90
    preco_acima_5kg = 5.80
elif tipo_carne == "Alcatra":
    preco_ate_5kg = 5.90
    preco_acima_5kg = 6.80
elif tipo_carne == "Picanha":
    preco_ate_5kg = 6.90
    preco_acima_5kg = 7.80
else:
    print("Tipo de carne inválido.")
    
if quantidade_kg <= 5:
    preco_total = quantidade_kg * preco_ate_5kg
else:
    preco_total = (5 * preco_ate_5kg) + ((quantidade_kg - 5) * preco_acima_5kg)

desconto = 0
if pagamento == "cartão":
    desconto = preco_total * 0.05

valor_a_pagar = preco_total - desconto

print("\nCupom Fiscal")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade de carne: {quantidade_kg:.2f} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {pagamento}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
