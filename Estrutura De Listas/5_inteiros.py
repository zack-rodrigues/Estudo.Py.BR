import random

vetor_inteiros = [random.randint(1, 100) for _ in range(5)]

soma = sum(vetor_inteiros)

multiplica = 1

for inteiro in vetor_inteiros:
    multiplica *= inteiro


print("Números do vetor:", vetor_inteiros)
print("A soma é:", soma)
print("A multiplicação é:", multiplica)


