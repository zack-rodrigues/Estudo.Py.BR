telefone = input("Telefone: ").replace("-", "").strip()

if len(telefone) == 7:
    print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
    telefone_corrigido = '3' + telefone
    print(f"Telefone corrigido sem formatação: {telefone_corrigido}")
    print(f"Telefone corrigido com formatação: {telefone_corrigido[:4]}-{telefone_corrigido[4:]}")
elif len(telefone) == 8:
    print("Telefone já possui 8 dígitos. Nenhuma correção necessária.")
else:
    print("Número inválido. Digite um número com 7 ou 8 dígitos.")
