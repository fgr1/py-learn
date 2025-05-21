peso = float(input("Digite seu peso em kg (ex.: 70.5): ").replace(',', '.'))
altura_cm = float(input("Digite sua altura em centímetros (ex.: 175): "))

altura_m = altura_cm / 100

imc = peso / (altura_m ** 2)

if imc < 18.5:
    condicao = "Abaixo do peso"
elif imc < 25:
    condicao = "Peso normal"
elif imc < 30:
    condicao = "Acima do peso"
else:
    condicao = "Obeso"

print(f"Seu IMC é {imc:.2f}.\nCondição: {condicao}.")
