from random import randint
computador =randint(0, 5)# faz o computador 'PENSAR'
print('vou pensar em um numero entre 0, 5... tente adivinhar')
jogador =int(input('em que numero pensei? '))# jogador tenta adivinhar
if jogador == computador:
    print('você acertou')
else:
    print(f'você errou, eu pensei no numero {computador} e nao no {jogador}')