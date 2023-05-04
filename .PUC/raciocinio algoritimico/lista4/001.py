estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
pedidos = []

while True:
    print("=== Cardápio ===")
    for produto, ingredientes in cardapio.items():
        print(f"{produto}: {', '.join(ingredientes)}")
    pedido = input("O que deseja pedir (0 para sair)? ")
    if pedido == '0':
        break
    elif pedido not in cardapio:
        print("Item não localizado no cardápio")
    else:
        ingredientes_faltantes = []
        for ingrediente in cardapio[pedido]:
            if estoque.get(ingrediente, 0) == 0:
                ingredientes_faltantes.append(ingrediente)
        if ingredientes_faltantes:
            for ingrediente in ingredientes_faltantes:
                print(f"Infelizmente acabou o {ingrediente}")
        else:
            for ingrediente in cardapio[pedido]:
                estoque[ingrediente] -= 1
            pedidos.append(pedido)
            print(f"Um {pedido} saindo no capricho!!!")

print("=== Pedido Finalizado ===")
print("Lanches pedidos:")
for pedido in pedidos:
    print(f"- {pedido}")
print("Ingredientes restantes em estoque:")
for ingrediente, quantidade in estoque.items():
    print(f"{ingrediente}: {quantidade}")
