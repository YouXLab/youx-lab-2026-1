import time

def titulo(msg):
    print('~'*len(msg))
    print(f' {msg} ')
    print('~'*len(msg))
    time.sleep(0.5)

def ajuda(com):
    titulo(f'Acessando o manual do comando {com}')
    help(com)

while True:
    titulo('Sistema de Ajuda PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('Até logo!')
        break
    ajuda(comando)