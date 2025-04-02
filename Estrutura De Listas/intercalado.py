A = [int(input(f"Digite o {i+1}º número do vetor A: ")) for i in range(10)]

B = [int(input(f"Digite o {i+1}º número do vetor B: ")) for i in range(10)]

C = [num for pair in zip(A, B) for num in pair]

print("\nVetor A:", A)
print("Vetor B:", B)
print("Vetor C (intercalado):", C)
