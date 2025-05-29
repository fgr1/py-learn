numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("\nNúmeros em ordem crescente:")
for n in numeros:
    print(n)
