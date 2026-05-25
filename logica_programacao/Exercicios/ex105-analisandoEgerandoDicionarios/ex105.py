def notas(*num, sit=False):
    cont = maior = menor = media = total = 0
    for c in num:
        cont += 1
        if c > maior:
            maior = c
        if c < menor or cont == 1:
            menor = c
        total += c
    media = total / cont
    if sit:
        print('A situação da turma é: ', end='')
        if media > 7:
            print('Boa!')
        elif media > 5:
            print('Rasoável')
        else:
            print('Ruim!')

