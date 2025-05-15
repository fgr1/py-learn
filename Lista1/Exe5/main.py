produto    = input("Digite o nome do produto: ")
valor_unit = float(input("Digite o valor unitário: R$ "))
quantidade = int(input("Digite a quantidade: "))

valor_total = valor_unit * quantidade

pagamento = input("Pagamento à vista? (S/N): ").strip().upper()

if pagamento == "S":
    desconto = valor_total * 0.15
    novo_total = valor_total - desconto
    print(f"\n{quantidade} × {valor_unit}: R$ {valor_total:.2f}")
    print(f"Desconto (15 % à vista): R$ {desconto:.2f}")
    print(f"Total a pagar: R$ {novo_total:.2f}")
else:
    print(f"\n{quantidade} × {valor_unit}: R$ {valor_total:.2f}")
    print(f"Total a pagar: R$ {valor_total:.2f}")
