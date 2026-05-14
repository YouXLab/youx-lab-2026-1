from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)
print('=====' * 50)
print('Jogo da tesoura,papel e pedra')
print('=====' * 50)
print('SUAS OPÇÕES:')
print('[0] PEDRA\n[1]PAPEL\n[2]TESOURA')
jogador = int(input('Qual será sua jogada?!:'))
print("Tesoura!")
sleep(2)
print('Papel!!')
sleep(2)
print('Pedra!!!')
sleep(2)
if computador == 0:
    if jogador == 0:
        print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]} portanto eu declaro:\n EMPATE!!!')
    elif jogador == 1:
        print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]},portanto eu declaro você como: VENCEDOR É O JOGADOR')
    elif jogador == 2:
        print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]},portanto eu declaro você como: PERDEDOR! O VENCEDOR É O COMPUTADOR!')
elif computador == 1:
    if jogador == 0:
        print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]},portanto eu declaro você como: PERDEDOR! O VENCEDOR É O COMPUTADOR!')
    elif jogador == 1:
        print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]} portanto eu declaro:\n EMPATE!!!')
    elif jogador == 2:
        print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]},portanto eu declaro você como: VENCEDOR É O JOGADOR')
elif computador == 2:
        if jogador == 0:
            print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]},portanto eu declaro você como: VENCEDOR É O JOGADOR')
        elif jogador == 1:
            print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]},portanto eu declaro você como: PERDEDOR! O VENCEDOR É O COMPUTADOR!')
        elif jogador == 2:
            print(f'O computador escolheu {itens[computador]} e você escolheu {itens[jogador]} portanto eu declaro:\n EMPATE!!!')
