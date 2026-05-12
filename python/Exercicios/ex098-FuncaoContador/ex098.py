from time import sleep
def cont(inicio, fim, passo):
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    for cont in range(inicio, fim +1, passo):
        print(f'{cont}', end=' ', flush=True)
        sleep(0.4)
    print()

cont(1, 10, 1)
cont(10, 0, -2)
print('Agora é sua vez! insira os valores de:')
print('-='*20)
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
cont(inicio, fim, passo)