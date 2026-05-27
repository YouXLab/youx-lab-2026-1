
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
nome = str(input('Olá! Qual seu nome? '))
print(f'Seja bem vindo[a] {nome}!')
opcao = 0
carrinho = []
while opcao != 4:
    print('''
    [1] Ver Cardápio e Avaliações
    [2] Adicionar Item ao Pedido
    [3] Finalizar Pedido
    [4] Sair do Sistema''')
    opcao = int(input('Escolha uma das opçoẽs: '))
    if opcao == 1:
      for i in cardapio:
          #print(i.items)
          print(i['id'])
          print(i['nome'])
          print(i['preco'])
    if opcao == 2:
        idpedido = int(input('Digite o ID do produto: '))
        quantidade_pedido = int(input('Qual a quantidade desejada do seu produto? '))
        for i in cardapio:
            if i['id'] == idpedido:
                achado = True
                i['quantidade'] = quantidade_pedido
                carrinho.append(i)
        if not achado:
            print('ID INVÁLIDO! TENTE NOVAMENTE. ')
    if opcao == 3:
        print("Gerando pedido e enviando para a cozinha...")
        print(f'{nome}, pediu: ')
        for i in carrinho:
            print(i['quantidade'], i['nome'])
    if opcao == 4:
      print('Até breve. Obrigada pela atenção e volte sempre!')
    if opcao > 4:
      print('ESTÁ OPÇÃO NÃO EXISTE. TENTE NOVAMENTE!')
