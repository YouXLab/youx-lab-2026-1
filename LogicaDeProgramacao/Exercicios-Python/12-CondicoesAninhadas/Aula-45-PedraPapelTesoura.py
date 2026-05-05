import random
print('Suas opções')
print('[1] Pedra ')
print('[2] Papel ')
print('[3] Tesoura ')
N1 = int(input('Qual sua jogada? '))

N2 = [1, 2, 3]

N3 = random.choice(N2)


print('-=-=-=-=-=-=-=-=-=-')
if N3 == 1:
    print('Robô jogou pedra')
elif N3 == 2:
    print('Robô jogou papel')
elif N3 == 3:
    print('Robô jogou tesoura')

if N1 == 1:
    print('Jogador jogou pedra')
elif N1 == 2:
    print('Jogador jogou papel')
elif N1 == 3:
    print('Jogador jogou tesoura')
print('-=-=-=-=-=-=-=-=-=-')

if N1 == 1 and N3 == 1:
    print('Empate')
elif N1 == 1 and N3 == 2:
    print('Robô ganhou')
elif N1 == 1 and N3 == 3:
    print('Jogador ganhou')

elif N1 == 2 and N3 == 2:
    print('Empate')
elif N1 == 2 and N3 == 1:
    print('Jogador ganhou')
elif N1 == 2 and N3 == 3:
    print('Robô ganhou')

elif N1 == 3 and N3 == 3:
    print('Empate')
elif N1 == 3 and N3 == 2:
    print('Jogador ganhou')
elif N1 == 3 and N3 == 2:
    print('Robô ganhou')
else:
    print('ERRO NUMERO INVALIDO')