from os import wait
from time import sleep

N1 = float(input('Digite um valor: '))
N2 = float(input('Digite outro valor: '))
P1 = N1 + N2
P2 = N1 * N2
print('[1] Somar')
print('[2] Multiplicar')
print('[3] maior')
print('[4] Novos numeros')
print('[5] Sair do programa')
R1 = int(input('Qual sua escolha? ').strip())
while R1 != 5:
    if R1 == 1:
        print(f'A soma entre {N1} e {N2} é igual a {P1}')
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] maior')
        print('[4] Novos numeros')
        print('[5] Sair do programa')
        R1 = int(input('Qual sua escolha? ').strip())
    elif R1 == 2:
        print(f'A multiplicação entre {N1} e {N2} é igual a {P2}')
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] maior')
        print('[4] Novos numeros')
        print('[5] Sair do programa')
        R1 = int(input('Qual sua escolha? ').strip())
    elif R1 == 3:
        if N1 > N2:
            print(f'O maior entre {N1} e {N2} é {N1}')
            print('[1] Somar')
            print('[2] Multiplicar')
            print('[3] maior')
            print('[4] Novos numeros')
            print('[5] Sair do programa')
            R1 = int(input('Qual sua escolha? ').strip())
        else:
            print(f'O maior entre {N1} e {N2} é {N2}')
            print('[1] Somar')
            print('[2] Multiplicar')
            print('[3] maior')
            print('[4] Novos numeros')
            print('[5] Sair do programa')
            R1 = int(input('Qual sua escolha? ').strip())
    elif R1 == 4:
        N1 = float(input('Digite um valor: '))
        N2 = float(input('Digite outro valor: '))
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] maior')
        print('[4] Novos numeros')
        print('[5] Sair do programa')
        R1 = int(input('Qual sua escolha? ').strip())
print('Finalizando...')
sleep(1)
print('==================//====================')
print('Fim.')
input()