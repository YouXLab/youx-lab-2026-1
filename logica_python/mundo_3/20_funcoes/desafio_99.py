from time import sleep

def maior( * numero):
    contagem = maior = 0
    print('~-~' * 20)
    print('\nAnalisando os valores passados. . .')
    for valor in numero:
        print(f'{valor}', end='')
        sleep(1)
        if contagem == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contagem += 1
    print(f'Foram informados {contagem} valores ao todo! ')
    print(f'O maior valor informado foi: {maior} ')

#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()