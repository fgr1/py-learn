palpite1 = input("Jogador 1 – Palpite (P para par / I para ímpar): ").strip().upper()
valor1   = int(input("Jogador 1 – Escolha um valor de 1 a 5: "))

if (palpite1 == 'P'):
    palpite2 = 'I'
    print("Jogador 2 – Palpite: Impar")
elif (palpite1 == 'I'):
    palpite2 = 'P'
    print("Jogador 2 – Palpite: Par")

valor2   = int(input("Jogador 2 – Escolha um valor de 1 a 5: "))

if not (1 <= valor1 <= 5) or not (1 <= valor2 <= 5):
    print("Rodada inválida: cada valor deve estar entre 1 e 5.")
    exit(1)

soma   = valor1 + valor2
parity = 'P' if soma % 2 == 0 else 'I'

if (palpite1 == parity) and (palpite2 != parity):
    vencedor = "Jogador 1"
elif (palpite2 == parity) and (palpite1 != parity):
    vencedor = "Jogador 2"
else:
    vencedor = "Empate"

tipo_soma = "par" if parity == 'P' else "ímpar"
print(f"Resultado ({tipo_soma}).\nVencedor: {vencedor}.")
