#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
operacao = 0
primeiro = int(input('primerio valor: '))
segundo = int(input('segundo valor: '))
while operacao != 5:
    print('''opçao:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    operacao = int(input('Qual a sua escolha: '))
    if operacao == 1:
        soma = primeiro + segundo
        print(f'A soma dos dois numeros é: {primeiro} + {segundo} = {soma}')
    if operacao == 2:
        mutiplicacao = primeiro * segundo
        print(f'A multiplicaçao dos dois numeros é: {primeiro} * {segundo} = {soma}')
    if operacao == 3:
        if primeiro > segundo:
            print(f'O primeiro é maior.')
        elif segundo > primeiro:
            print(f'O segundo é maior')
    if operacao == 4:
        primeiro = int(input('primerio valor: '))
        segundo = int(input('segundo valor: '))




