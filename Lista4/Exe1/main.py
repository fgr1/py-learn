estoque = {
    'pao': 10,
    'hamburguer': 12,
    'tomate': 5,
    'bacon': 5,
    'ovo': 5
}

cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

def imprimir_cardapio():
    print("\n--- CARDÁPIO BOCA FELIZ ---")
    for item in cardapio:
        print(f"- {item}")
    print("---------------------------")

def verificar_ingredientes(pedido):
    faltando = []
    ingredientes = cardapio[pedido]
    ingredientes_usados = {}

    for item in ingredientes:
        ingredientes_usados[item] = ingredientes_usados.get(item, 0) + 1

    for ingrediente, quantidade_necessaria in ingredientes_usados.items():
        if estoque.get(ingrediente, 0) < quantidade_necessaria:
            faltando.append(ingrediente)
    
    return faltando, ingredientes_usados

def preparar_pedido(pedido):
    faltando, ingredientes_usados = verificar_ingredientes(pedido)

    if faltando:
        for item in faltando:
            print(f"Infelizmente acabou o {item}")
    else:
        for ingrediente, qtd in ingredientes_usados.items():
            estoque[ingrediente] -= qtd
        print(f"Um {pedido} saindo no capricho!!!")

while True:
    imprimir_cardapio()
    pedido = input("O que deseja pedir (0 para sair)? ").strip().lower()

    if pedido == "0":
        print("Volte sempre!")
        break
    elif pedido not in cardapio:
        print("Item não loco no cardápializado.\n")
    else:
        preparar_pedido(pedido)
