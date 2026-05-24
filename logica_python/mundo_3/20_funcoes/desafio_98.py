
from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        contagem = inicio
        while contagem <= fim:
            print(f'{contagem}', end='', flush=True)
            sleep(0.5)
        contagem += passo
        print('FIM!!!!!')
    else:
        contagem = inicio
        while contagem >= fim:
            print(f'{contagem} ', end='', flush=True)
            sleep(0.5)
            contagem -= passo
        print('FIM!!!!')
contador(10, 0, 2)