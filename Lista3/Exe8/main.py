while True:
    binario = input("Digite um número em binário: ").strip()

    if all(b in '01' for b in binario) and binario != "":
        decimal = int(binario, 2)
        print(f"Decimal de {binario} é {decimal}")
        break
    else:
        print("Digite apenas números binários (0 e 1).\n")
