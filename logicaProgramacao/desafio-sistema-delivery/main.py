from time import sleep
from cardapio import cardapio

def verMedia(produto):
    soma = sum(produto['avaliacoes'])
    cont = len(produto['avaliacoes'])
    produto['media'] = soma / cont
    print(f'''
id: {produto['id']},
nome: {produto['nome']},
preço: R$ {produto['preco']},
media avaliações: {produto['media']:.2f}
                    ''')

def buscar(id):
    for i in cardapio:
        if i['id'] == id:
            return i

def subtotal(lista):
    soma = 0
    for i in lista:
        soma += i['preco'] * i['quantidade']
    return soma



cart = []
pedido_final = {}


print(" OLÁ, BEM VINDO!")
sleep(1)
print('para começar-mos, me deixe te conhecer melhor...')
sleep(1)
nome = str(input('Qual seu nome?: ').strip())
print(f'Perfeito!, Prazer em te conhecer {nome}')
opcao = 0
while opcao != 4:
    print('''
[1] Ver Cardápio e Avaliações
[2] Adicionar Item ao Pedido
[3] Finalizar Pedido
[4] Sair do Sistema
    ''')
    opcao = int(input('Digite uma opção: '))
    if opcao not in (1,2,3,4):
        while opcao not in (1,2,3,4):
            print('Opção invalida!, digite um número de 1 a 4')
            opcao = int(input('Digite uma opção: '))
    else:
        if opcao == 1:
            for cont, produto in enumerate(cardapio):
                print('-='*10, f' < PRODUTO {cont+1} > ', '-='*10)
                verMedia(produto)
        elif opcao == 2:
            escolhido = int(input('Digite o id do produto que deseja: '))
            while not buscar(escolhido):
                print('Não possuimos um produto com esse id')
                escolhido = int(input('Digite o id do produto que deseja: '))
            quantidade = int(input(f'Quantos {buscar(escolhido)["nome"]} você deseja?: '))
            cart.append({'id': escolhido, 'quantidade': quantidade, 'preco': buscar(escolhido)["preco"]})
        elif opcao == 3:
            if len(cart) <= 0:
                print('Erro! nenhum item adicionado!')
            else:
                if subtotal(cart) > 75:
                    totalFinal = subtotal(cart) - (subtotal(cart)*(15 / 100))
                elif subtotal(cart) >= 50:
                    totalFinal = subtotal(cart) - (subtotal(cart)*(10 / 100))
                else:
                    totalFinal = subtotal(cart)
                totalFinal += 6
                pedido_final = {
                    'nome_cliente': nome,
                    'itens': cart,
                    'subtotal': subtotal(cart),
                    'valor_entrega': 6,
                    'valor_total': totalFinal
                }
                opcao = 4
if pedido_final:
    print("Gerando pedido e enviando para a cozinha...")
    print(pedido_final)