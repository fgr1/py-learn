produto    = input("Digite o nome do produto: ")
valor_unit = float(input("Digite o valor unitário: R$ "))
quantidade = int(input("Digite a quantidade: "))

valor_total = valor_unit * quantidade

print(f"O valor total {quantidade} × {valor_unit} = R$ {valor_total:.2f}")
