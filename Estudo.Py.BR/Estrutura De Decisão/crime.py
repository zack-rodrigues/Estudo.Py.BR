resposta1 = input("Telefonou para a vítima? (s/n): ").strip().lower()
resposta2 = input("Esteve no local do crime? (s/n): ").strip().lower()
resposta3 = input("Mora perto da vítima? (s/n): ").strip().lower()
resposta4 = input("Devia para a vítima? (s/n): ").strip().lower()
resposta5 = input("Já trabalhou com a vítima? (s/n): ").strip().lower()

respostas_positivas = sum([
    resposta1 == "s",
    resposta2 == "s",
    resposta3 == "s",
    resposta4 == "s",
    resposta5 == "s"
])

if respostas_positivas == 5:
    classificacao = "Assassino"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

print("Classificação final: " + classificacao)
