def maior(*num):
    maior = cont = 0
    print('Analisando os numeros')
    for valor in num:

        print(f'{valor}',end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'O maior valor informado foi {maior}')







maior(8,7,2,3,9,1,4)
maior(0,4,6)
maior(5,1,8,7)
maior(9,7,1,2)