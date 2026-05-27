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
opcao = 0
nome = str(input('Digite seu nome: '))
print("Boas vindas")
print("""
[1] Ver Cardápio e Avaliações
[2] Adicionar Item ao Pedido
[3] Finalizar Pedido
[4] Sair do Sistema""")
opcao = int(input('>>>> Qual é a opção? '))
#voltarei todas as opções depois
if opcao == 1:
    for elemento in cardapio:
         print(elemento)
    for item in cardapio:
        print(item["id"], end=' ')

    for nome in cardapio:
        print(nome["nome"], end=' ')

    for preco in cardapio:
        print(preco["preco"], end=' ')

    for avaliacoes in cardapio:
        print(avaliacoes["avaliacoes"], end=' ')

