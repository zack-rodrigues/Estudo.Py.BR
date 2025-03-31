def obter_valor_inteiro(mensagem, condicao=lambda x: x > 0, erro="Insira um número inteiro positivo."):
    while True:
        try:
            valor = int(input(mensagem))
            if condicao(valor):
                return valor
            print(erro)
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")

def obter_valor_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor / 100  # Convertendo para decimal
            print("A taxa de crescimento deve ser um número positivo.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

def calcular_anos(pais_a, taxa_a, pais_b, taxa_b):
    anos = 0
    while pais_a < pais_b:
        pais_a += pais_a * taxa_a
        pais_b += pais_b * taxa_b
        anos += 1
    return anos

# Coletando dados
pais_a = obter_valor_inteiro("Defina a população do país A: ")
pais_b = obter_valor_inteiro("Defina a população do país B: ", lambda x: x > pais_a, "A população do país B deve ser maior que a do país A.")
taxa_a = obter_valor_float("Defina a taxa de crescimento do país A (em %): ")
taxa_b = obter_valor_float("Defina a taxa de crescimento do país B (em %): ")

# Calculando e exibindo resultado
anos = calcular_anos(pais_a, taxa_a, pais_b, taxa_b)
print(f"O país A ultrapassará ou igualará o país B em população em {anos} anos.")
