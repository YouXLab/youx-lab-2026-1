import random

print('vamos jogar pedra papel e tesoura')
jogador = str(input('pedra, papel ou tesoura'))
computador = random.choice(['Pedra', 'Papel', 'tesoura: ']).lower()
print(f'Voce escolheu {jogador}')
print(f'O computador escolheu {computador}')
if jogador == computador:
    print('Empate')
elif (jogador == 'pedra' and computador == 'tesoura'):
    print('Voce ganhou!')
elif (jogador == 'tesoura' and computador == 'papel'):
    print('Voce ganhou!')
elif (jogador == 'pepel' and computador == 'pedra'):
    print('Voce ganhou!')
else:
    print('Computador ganhou!')

