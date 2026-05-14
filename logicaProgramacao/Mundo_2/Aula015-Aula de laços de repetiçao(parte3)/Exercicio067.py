numero = 0
while numero >= 0:
    numero = int(input('Digite um numero para ver sua tabuada: '))
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(numero, c, numero * c))
print('PROGRAMA ENCERRADO! VOLTE SEMPRE! ')