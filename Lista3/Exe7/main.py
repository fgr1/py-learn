contador_a = 0

while True:
    palavra = input("Digite uma palavra (Enter para sair): ").strip()

    if palavra == "":
        break

    contador_a += palavra.lower().count('a')

print(f"\nLetras 'A' encontradas: {contador_a}")
