ano_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557609.92
}

unidades = [
    "Parsec (pc)",
    "Ano-Luz (al)",
    "Unidade Astronômica (ae)",
    "Minuto-Luz (ml)",
    "Segundo-Luz (sl)"
]

print("\n------- Conversor -------")
print("Unidades disponíveis:")
for u in unidades:
    print(f"- {u}")

while True:
    try:
        valor = float(input("\nValor a ser convertido: "))
        break
    except ValueError:
        print("Digite um número válido!")

origem = input("Converter de (abreviação): ").strip().lower()

destino = input("Converter para (abreviação): ").strip().lower()

if origem not in ano_luz or destino not in ano_luz:
    print("Unidade inválida! Use as abreviações corretas: pc, al, ae, ml, sl")
else:
    valor_em_al = valor * ano_luz[origem]
    valor_convertido = valor_em_al / ano_luz[destino]

    print(f"\nConversão: {valor} {origem} = {valor_convertido:.6f} {destino}")
