from time import sleep

def maior(*numero):
    contagem = maior = 0
    maior = 0

    print('\nAnalisando os valores passados...')

    for valor in numero:
        print(f'{valor} ', end='')
        sleep(0.5)

        if contagem == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor

        contagem += 1

    print(f'Foram informados {contagem} valores ao todo')
    print(f'O maior valor informado foi {maior}')

# programa principal
maior(2, 9, 4, 5, 7, 1)
