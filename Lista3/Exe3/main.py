def vencedor(jogada1, jogada2):
    if jogada1 == jogada2:
        return 0  # empate
    elif (jogada1 == "pedra" and jogada2 == "tesoura") or \
         (jogada1 == "papel" and jogada2 == "pedra") or \
         (jogada1 == "tesoura" and jogada2 == "papel"):
        return 1
    else:
        return 2 

pontos_para_vencer = int(input("Quantos pontos para vencer? "))

pontos_j1 = 0
pontos_j2 = 0

while pontos_j1 < pontos_para_vencer and pontos_j2 < pontos_para_vencer:
    print("\n--- Nova rodada ---")
    jogada1 = input("Jogador 1, escolha (pedra, papel, tesoura): ").lower()
    jogada2 = input("Jogador 2, escolha (pedra, papel, tesoura): ").lower()

    if jogada1 not in ["pedra", "papel", "tesoura"] or jogada2 not in ["pedra", "papel", "tesoura"]:
        print("Jogada inválida! Tente novamente.")
        continue

    resultado = vencedor(jogada1, jogada2)

    if resultado == 0:
        print("Empate!")
    elif resultado == 1:
        print("Jogador 1 vence a rodada!")
        pontos_j1 += 1
    else:
        print("Jogador 2 vence a rodada!")
        pontos_j2 += 1

    print(f"Placar: Jogador 1 - {pontos_j1} | Jogador 2 - {pontos_j2}")

if pontos_j1 == pontos_para_vencer:
    print("\n Jogador 1 venceu o jogo!")
else:
    print("\n Jogador 2 venceu o jogo!")
