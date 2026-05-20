total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto:'))
    preco = float(input('Preco: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
     if preco < menor:
        menor = preco
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp == 'N':
            break
    print('{:-^40}'.format('FIM DO PROGRAMA'))
    print(f'O total da compra foi R${total:.2f}')