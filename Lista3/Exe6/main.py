while True:
    nome = input("Digite seu nome completo: ").strip()
    partes = nome.split()

    if len(partes) >= 2:
        primeiro = partes[0]
        ultimo = partes[-1]
        print(f"\nPrimeiro nome: {primeiro}")
        print(f"Último nome: {ultimo}")
        break
    else:
        print("Digite pelo menos um nome e um sobrenome.\n")
