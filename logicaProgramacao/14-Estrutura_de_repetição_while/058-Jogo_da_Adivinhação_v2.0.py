from random import randint
computador =randint (0, 10)
print('sou seu computador...\nacabei de pensar em um numero de 0, 10.\nsera que voce consegue adivinhar qual foi?')
acerto = False
tentativas = 0
while not acerto:
    jogador =int(input('qual seu palpite?'))
    tentativas += 1
    if jogador > computador:
        print('menos...tente mais uma vez')
    elif jogador < computador:
        print('mais...tente mais una vez')
    elif computador == jogador:
        acerto = True
print(f'voce digitou {tentativas}  numeros para acertar')
print('acertou')