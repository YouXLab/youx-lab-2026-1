cardapio = [
    {
        "id": 1,
        "nome": "Hambúrguer Clássico",
        "preco": 25.50,
        "avaliacoes": [5, 4, 5]
    },
    {
        "id": 2,
        "nome": "Pizza Margherita",
        "preco": 45.00,
        "avaliacoes": [5, 5, 4, 4, 5, 4]
    },
    {
        "id": 3,
        "nome": "Batata Frita",
        "preco": 15.00,
        "avaliacoes": [3, 4]
    },
    {
        "id": 4,
        "nome": "Refrigerante Lata",
        "preco": 8.00,
        "avaliacoes": [5, 5, 5, 4]
    },
    {
        "id": 5,
        "nome": "Cachorro Quente Prensado",
        "preco": 18.90,
        "avaliacoes": [4, 4, 5, 3]
    },
    {
        "id": 6,
        "nome": "Suco de Laranja Natural",
        "preco": 12.00,
        "avaliacoes": [5, 5, 5]
    },
    {
        "id": 7,
        "nome": "Sorvete de Baunilha",
        "preco": 14.50,
        "avaliacoes": [5, 4, 5, 5]
    },
    {
        "id": 8,
        "nome": "Porção de Onion Rings",
        "preco": 22.00,
        "avaliacoes": [4, 3, 4, 4, 5]
    },
    {
        "id": 9,
        "nome": "Salada Caesar",
        "preco": 28.00,
        "avaliacoes": [5, 5, 4]
    },
    {
        "id": 10,
        "nome": "Brownie de Chocolate",
        "preco": 16.00,
        "avaliacoes": [5, 5, 5, 5, 4]
    }
]

nome = input("Qual seu nome: ");
print('--' * 35)
print("BOAS VINDAS " + nome)
print('--' * 35)
print('OPÇÕES CARDAPIO')
opcao = 0
carrinho = []
while opcao != 4:
    print('''
    [1] Ver Cardápio e Avaliações
    [2] Adicionar Item ao Pedido
    [3] Finalizar Pedido
    [4] Sair do Sistema ''')
    print('--' * 35)

    opcao = int(input('qual opção você prefere?  '))
    if opcao == 1:
        for comida in cardapio:
            print(f"ID:{comida['id']}/ NOME:{comida['nome']}/ PREÇO DO PRODUTO:{comida['preco']:.2f}")
        #calcular a média(se der tempo)
    if opcao == 2:
        novo_id = int(input('digite o ID do produto desejado: '))
        for item_cardapio in cardapio:
            if novo_id == item_cardapio["id"]:
                quantidade = int(input('digite a quantidade de itens do produto: '))
                novo_item_carrinho = {
                    'nome': item_cardapio['nome'],
                    'preco': item_cardapio['preco'],
                    'quantidade': quantidade
                }
                carrinho.append(novo_item_carrinho)
        print(carrinho)

    if opcao == 3:
        print(carrinho)
        soma = 0
        for produto in carrinho:
            soma += produto['preco'] * produto['quantidade']

        print(soma)
        if soma > 75:
            total = soma - ((soma * 1.15) - soma)

        elif soma >= 50:
            total = soma - ((soma * 1.10) - soma)

        print(f'{nome} pediu ', end='')
        for i in carrinho:
            print(i['quantidade'], i['nome'])

