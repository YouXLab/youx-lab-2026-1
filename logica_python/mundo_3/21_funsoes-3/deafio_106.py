
from time import sleep

while True:
    print('\033[1;32m-=' * 20)
    print('  SISTEMA DE AJUDA PYTHON')
    print('-=' * 20)

    cmd = input('\033[mFunção ou Biblioteca > ')

    if cmd.upper() == 'FIM':
        break

    print(f'\033[1;34mBuscando ajuda sobre "{cmd}"...\033[m')
    sleep(1)

    help(cmd)

print('\033[1;31mPROGRAMA ENCERRADO!\033[m')