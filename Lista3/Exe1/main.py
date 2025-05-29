massa = float(input("Informe a massa inicial em gramas: "))

tempo = 0

while massa >= 0.5:
    massa /= 2
    tempo += 50

print(f"Massa final: {massa:.4f} gramas")
print(f"Tempo total: {tempo} segundos")
