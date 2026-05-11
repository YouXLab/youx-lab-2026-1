from time import sleep


def titulo(msgm):
    tam = len(msgm)
    print('~'*tam)
    print(f'{msgm}')
    print('~'*tam)
    sleep(0.5)

def ajuda(com):
    titulo(f'Acessando o manual do comando {com}')
    help(com)

while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca -> '))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!')
        break
    ajuda(comando)