n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('→ Qual a opção? '))
    if opcao == 1:
        print('a soma entre {} + {} = {}'.format(n1, n2, n1+n2))
    if opcao == 2:
        print('a multiplicação entre {} x {} = {}'.format(n1, n2, n1*n2))
    if opcao == 3:
        if n1 > n2:
            print('O maior valor é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    if opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    if opcao == 5:
        print('Finalizando...')
    print('-=' *10)
print('Programa finalizado')