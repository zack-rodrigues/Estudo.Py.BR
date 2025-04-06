cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ")

if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    numeros = cpf.replace('.', '').replace('-', '')
    if numeros.isdigit() and len(set(numeros)) > 1:
        soma1 = sum(int(numeros[i]) * (10 - i) for i in range(9))
        dig1 = (soma1 * 10 % 11) % 10
        soma2 = sum(int(numeros[i]) * (11 - i) for i in range(10))
        dig2 = (soma2 * 10 % 11) % 10
        if dig1 == int(numeros[9]) and dig2 == int(numeros[10]):
            print("CPF VÁLIDO ✅")
        else:
            print("CPF INVÁLIDO ❌")
    else:
        print("CPF INVÁLIDO ❌")
else:
    print("Formato inválido ❌")


#ou

def validar_cpf(cpf):
    # Verifica se está no formato correto
    if len(cpf) != 14 or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False

    # Remove pontos e traço
    cpf_numeros = cpf.replace('.', '').replace('-', '')

    # Verifica se tem exatamente 11 dígitos numéricos
    if not cpf_numeros.isdigit() or len(cpf_numeros) != 11:
        return False

    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
    if cpf_numeros == cpf_numeros[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf_numeros[i]) * (10 - i)
    resto1 = (soma1 * 10) % 11
    if resto1 == 10:
        resto1 = 0

    # Verifica o primeiro dígito
    if resto1 != int(cpf_numeros[9]):
        return False

    # Calcula o segundo dígito verificador
    soma2 = 0
    for i in range(10):
        soma2 += int(cpf_numeros[i]) * (11 - i)
    resto2 = (soma2 * 10) % 11
    if resto2 == 10:
        resto2 = 0

    # Verifica o segundo dígito
    if resto2 != int(cpf_numeros[10]):
        return False

    return True

# Programa principal
cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

if validar_cpf(cpf):
    print("CPF VÁLIDO ✅")
else:
    print("CPF INVÁLIDO ❌")
