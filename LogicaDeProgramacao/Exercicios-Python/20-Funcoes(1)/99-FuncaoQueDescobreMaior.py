def maior(* núm):
    cont = big = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(valor,end=' ',flush=True)
        if cont == 0:
            big = valor
        else:
            if valor > big:
                big = valor
        cont += 1
    print(f'Foram informados {cont} valores a todo. ')
    print(f'O maior valor foi {big}.')

maior(1,2,3,4,5,6)