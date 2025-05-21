while True:
    cpf = input("Digite os 11 dígitos do CPF: ").strip()
    cpf_digitos = [c for c in cpf if c.isdigit()]

    if len(cpf_digitos) == 11:
        digitos = list(map(int, cpf_digitos))
        break
    print("Entrada inválida: é preciso ter exatamente 11 dígitos.\n")

if len(set(digitos)) == 1:
    print("\nCPF inválido: todos os dígitos são iguais.")
    exit(1)

soma1 = 0
for idx in range(9):
    soma1 += digitos[idx] * (10 - idx)

resto1 = (soma1 * 10) % 11
if resto1 == 10:
    resto1 = 0

soma2 = 0
for idx in range(10):
    soma2 += digitos[idx] * (11 - idx)

resto2 = (soma2 * 10) % 11
if resto2 == 10:
    resto2 = 0

valido = (resto1 == digitos[9]) and (resto2 == digitos[10])

cpf_formatado = (
    f"{digitos[0]}{digitos[1]}{digitos[2]}."
    f"{digitos[3]}{digitos[4]}{digitos[5]}."
    f"{digitos[6]}{digitos[7]}{digitos[8]}-"
    f"{digitos[9]}{digitos[10]}"
)

print(f"\nCPF: {cpf_formatado} é {'VÁLIDO' if valido else 'INVÁLIDO'}")
