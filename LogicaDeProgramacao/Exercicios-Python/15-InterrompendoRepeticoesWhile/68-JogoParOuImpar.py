import random
print('Este jogo é de Par ou Impar [Escolha um numero de 1 a 10')
cont = 0
while True:
     N1 = random.randint(1, 10)
     print(f'Computador escolheu {N1}')
     N2 = float(input('Escreva um numero: '))
     N3 = str(input('Escolha [P/I]: ').strip().upper())
     C1 = N1 + N2
     C2 = float(str(C1)[-3])
     if N3 in 'Ii' and C2 in [1,3,5,7,9]:
        print('Jogador venceu')
        cont = cont + 1
     elif N3 in 'Pp' and C2 in [0,2,4,6,8]:
        print('Jogador vence')
        cont = cont + 1
     else:
        print('Computador vence')
        cont = cont + 1
        break
if cont == 1:
    print(f'Você perdeu em  {cont} partida, LOSER!!!!!')
else:
 print(f'Você perdeu em  {cont} partidas, LOSER!!!!!')