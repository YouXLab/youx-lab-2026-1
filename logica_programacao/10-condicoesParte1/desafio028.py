from random import randint
computador =randint(0,5)
print('-=-' * 25 )
print('Vou pensar em um número entre 0 e 5...Tente adivinhar...')
print('-=-' * 25 )
jogador =int(input('Em que número eu pensei...?'))
if jogador == computador:
    print('Parabéns você acertou e ganhou um abraço!!!')
else:
    print('Seu loseeeeeeeeeeeeeeeeerrrrrr!!!!!', f'Então,eu pensei em {computador} e você pensou em {jogador}' )

