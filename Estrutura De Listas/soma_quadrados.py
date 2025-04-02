A = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]

soma_quadrados = sum(x**2 for x in A)

print("A soma dos quadrados dos elementos é:", soma_quadrados)