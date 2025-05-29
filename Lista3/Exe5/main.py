pop_a = 5000000
pop_b = 7000000

taxa_a = 0.03
taxa_b = 0.02

anos = 0

while pop_a <= pop_b:
    pop_a += pop_a * taxa_a
    pop_b += pop_b * taxa_b
    anos += 1

print(f"País A passa o país B em {anos} anos.")
print(f"População final de A: {int(pop_a)}")
print(f"População final de B: {int(pop_b)}")
