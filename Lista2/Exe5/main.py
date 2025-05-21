
precos = {
    "norte":        (500.00, 900.00),
    "nordeste":     (350.00, 650.00),
    "centro-oeste": (350.00, 600.00),
    "sul":          (300.00, 550.00),
}

destino = input("Região de destino (Norte, Nordeste, Centro-Oeste, Sul): ").strip().lower()

while True:
    destino = input("Região de destino (Norte, Nordeste, Centro-Oeste, Sul): ").strip().lower()

    if destino in precos:
        break
    print("Destino inválido! Tente novamente.\n")

ida_volta = input("A viagem inclui retorno (ida e volta)? (S para sim / N para não): ").strip().upper()

while True:
    ida_volta = input("A viagem inclui retorno (ida e volta)? (S para sim / N para não): ").strip().upper()

    if ida_volta in ("S", "N"):
        break
    print("Resposta inválida! Digite S ou N.\n")

preco_ida, preco_ida_volta = precos[destino]
preco_final = preco_ida_volta if ida_volta == "S" else preco_ida

tipo_viagem = "ida e volta" if ida_volta == "S" else "somente ida"
print(f"\nDestino: {destino.title()} — Viagem: {tipo_viagem}")
print(f"Preço da passagem: R$ {preco_final:.2f}")
