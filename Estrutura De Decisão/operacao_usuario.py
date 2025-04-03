num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = input("Digite o número da operação desejada: ")

if opcao == "1":
    resultado = num1 + num2
    operacao = "soma"
elif opcao == "2":
    resultado = num1 - num2
    operacao = "subtração"
elif opcao == "3":
    resultado = num1 * num2
    operacao = "multiplicação"
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        operacao = "divisão"
    else:
        print("Erro: Divisão por zero não é permitida.")
        exit()
else:
    print("Opção inválida!")
    exit()

print(f"O resultado da {operacao} é {resultado}")

if resultado % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

if resultado > 0:
    sinal = "positivo"
elif resultado < 0:
    sinal = "negativo"
else:
    sinal = "neutro"

if resultado == int(resultado):
    tipo = "inteiro"
else:
    tipo = "decimal"

print(f"O número {resultado} é {paridade}, {sinal} e {tipo}.")
