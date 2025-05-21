altura_cm = float(input("Digite sua altura em centímetros: "))
sexo = input("Digite seu sexo (M para homem / F para mulher): ").strip().upper()

altura_m = altura_cm / 100

if sexo == 'M':
    peso_ideal = 72.7 * altura_m - 58
elif sexo == 'F':
    peso_ideal = 62.1 * altura_m - 44.7
else:
    print("Sexo inválido. Digite 'M' para homem ou 'F' para mulher.")
    exit(1)

print(f"Peso ideal é {peso_ideal:.2f} kg.")
