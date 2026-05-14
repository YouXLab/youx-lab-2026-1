primeiro =int(input('primeiro valor: '))
segundo =int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1]soma
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa''')
    opcao =int(input('qual sua opção? '))
    if opcao == 1:
        s = primeiro + segundo
        print(f'a soma entre {primeiro} e {segundo} é {s}')
    elif opcao == 2:
        produto = primeiro * segundo
        print(f'o resultado entre {primeiro} x {segundo} é {produto}')
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('o  maior valor digitado foi', max(primeiro, segundo))
    elif opcao == 4:
        variavel =int(input('novo numero: '))
        novo =int(input('novo numero: '))
    elif opcao == 5:
        print('opção invalida, tente novamente!')
else:
    print('fim do programa!, volte sempre!')