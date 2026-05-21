from time import sleep
# def contador(num):
#     print('Contagem de 1 á 10 de 1 em 1:')
#     for c in range(1, 10+1):
#         print(c, end=' ')
#         sleep(0.5)
#     print('\n' + '-='*30)
#     print('Contagem de 1 á 10 de 1 em 1:')
#     for c in range(10, -1 , -2):
#         print(c, end=' ')
#         sleep(0.5)
#     print('\n' + '-=' * 30)
#     print('Agora é sua vez de personalizar a contagem!')
#     inicio = int(input('Início: '))
#     fim = int(input('Fim: '))
#     passos = int(input('Passos: '))
#     print('-='*30)
#     print(f'Contagem de {inicio} á {fim} de {passos} em {passos}:')
#     for c in range(inicio,fim + 1,passos):
#         print(c, end=' ')
#         sleep(0.5)
#     print(' Fim.')
# contador(num=True)
def contador(i,f,p):
    print(f'Contagem de {i} a {f} de {p} em {p}')
    for c in range(i,f,p):
        print(c, end=' ')
        sleep(0.5)
    print('Fim.')
contador(1,10,1)
contador(10,1,-2)
ini = int(input('Inicío:'))
fim = int(input('Fim:'))
pas = int(input('Passo:'))
contador(ini,fim,pas)