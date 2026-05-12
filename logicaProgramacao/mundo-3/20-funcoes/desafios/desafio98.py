import time

def contador(a, b, c):
    print('-='*30)
    if c < 0:
        c = c * -1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c == 0:
        c = 1
    if a > b:
        c = -c
    for n in range(a, b+c, c):
        print(n , end=' ')
        print('', end='')
        time.sleep(0.5)
    print('Fim!')
    print('-='*30)
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)