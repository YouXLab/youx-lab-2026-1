#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.


def titulo(cor=0, cabecalho=''):
    tamanho = 2 * len(cabecalho)
    print(f'\033[{cor}m' + '-' * tamanho)
    print(f'{cabecalho:^{tamanho}}')
    print('-' * tamanho)
    print('\033[m', end='')


def ajuda(busca=''):
    biblioteca = ''

    while biblioteca != 'fim':
        biblioteca = str(input(busca)).strip().lower()

        if biblioteca != 'fim':
            titulo(104, f'Acessando o manual do comando "{biblioteca}"')
            print('\033[7m')
            help(biblioteca)
            print('\033[m', end='')


# Programa Principal
titulo(46, 'SISTEMA DE AJUDA PyHELP')
ajuda('Função ou biblioteca > ')
titulo(101, 'PROGRAMA ENCERRADO!')