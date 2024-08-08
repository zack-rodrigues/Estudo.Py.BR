pop_a = 80000
taxa_a = 3  
pop_b = 200000
taxa_b = 1.5 

taxa_a /= 100
taxa_b /= 100

anos = 0

while pop_a < pop_b:
    pop_a += pop_a * taxa_a
    pop_b += pop_b * taxa_b
    anos += 1

print(f"A população do país A ultrapassará ou igualará apopulação do país B em {anos} anos.")
