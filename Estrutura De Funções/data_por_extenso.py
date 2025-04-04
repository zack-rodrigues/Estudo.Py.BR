def data_por_extenso(data):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    try:
        dia, mes, ano = map(int, data.split('/'))
        if 1 <= mes <= 12 and 1 <= dia <= 31:
            return f"{dia} de {meses[mes - 1]} de {ano}"
        else:
            return "Data inválida"
    except ValueError:
        return "Formato inválido"


def main():
    data = input("Digite uma data (DD/MM/AAAA): ")
    print(data_por_extenso(data))


main()
