def valorPagamento(valor, dias_atraso):
   
    if dias_atraso > 0:
        multa = valor * 0.03
        juros = valor * (0.001 * dias_atraso)
        return valor + multa + juros
    return valor


def main():
    total_prestacoes = 0
    total_valor = 0
    
    while True:
        valor = float(input("Digite o valor da prestação (ou 0 para sair): "))
        if valor == 0:
            break
        
        dias_atraso = int(input("Digite o número de dias em atraso: "))
        valor_final = valorPagamento(valor, dias_atraso)
        print(f"Valor a ser pago: R$ {valor_final:.2f}\n")
        
        total_prestacoes += 1
        total_valor += valor_final
    
    print("\n--- RELATÓRIO DO DIA ---")
    print(f"Total de prestações pagas: {total_prestacoes}")
    print(f"Valor total pago: R$ {total_valor:.2f}")

main()
