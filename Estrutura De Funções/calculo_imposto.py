def somaImposto(taxaImposto, custoBruto):
    imposto = custoBruto * (taxaImposto / 100)
    precoFinal = custoBruto + imposto
    print(f'O preço com imposto é: R$ {precoFinal:.2f}')

taxaImposto = float(input('Digite a taxa de imposto (%): '))
custoBruto = float(input('Digite o custo inicial (R$): '))

somaImposto(taxaImposto, custoBruto)
