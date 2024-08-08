while True:
    try:
        pop_A = float(input("Informe a população do país A: "))
        taxa_A = float(input("Informe a taxa de crescimento anual do país A (em %): ")) / 100
        pop_B = float(input("Informe a população do país B: "))
        taxa_B = float(input("Informe a taxa de crescimento anual do país B (em %): ")) / 100

        if pop_A <= 0 or taxa_A < 0 or pop_B <= 0 or taxa_B < 0:
            print("Valores inválidos. As populações e taxas devem ser positivas.")
            continue

        anos = 0
        while pop_A < pop_B:
            pop_A += pop_A * taxa_A
            pop_B += pop_B * taxa_B
            anos += 1

        print(f"Anos necessários para a população do país A ultrapassar ou igualar a população do país B: {anos}")

    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

    repetir = input("Deseja realizar outra simulação? (s/n): ").strip().lower()
    if repetir != 's':
        break
