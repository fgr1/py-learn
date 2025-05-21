preco = float(input("Digite o preço do produto: ").replace(',', '.'))

print(
    "\nCondições de pagamento:"
    "\n1 – À vista em dinheiro ou cheque (10% de desconto)"
    "\n2 – À vista no cartão de crédito (15% de desconto)"
    "\n3 – Em duas vezes (preço normal, sem juros)"
    "\n4 – Em três ou mais vezes (preço normal + 10% de juros)"
)

codigo = int(input("\nEscolha o código da condição de pagamento: "))

if codigo == 1:
    total = preco * 0.90
    print(f"\nTotal a pagar: R$ {total:.2f} (10 % de desconto).")

elif codigo == 2:
    total = preco * 0.85
    print(f"\nTotal a pagar: R$ {total:.2f} (15 % de desconto).")

elif codigo == 3:
    parcela = preco / 2
    print(f"\nPagamento em 2x de R$ {parcela:.2f} (sem juros). Total: R$ {preco:.2f}.")

elif codigo == 4:
    total = preco * 1.10
    while True:
        n_parcelas = int(input("Quantidade de parcelas (mínimo 3): "))
        if n_parcelas >= 3:
            break
        print("Número de parcelas inválido. Tente novamente (mínimo 3).")

    parcela = total / n_parcelas
    print(
        f"\nPagamento em {n_parcelas}x de R$ {parcela:.2f} "
        f"(total com 10 % de juros: R$ {total:.2f})."
    )

else:
    print("\nCódigo de condição de pagamento inválido.")
