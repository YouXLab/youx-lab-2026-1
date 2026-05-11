from random import randint
print('suas opcoes, [1] pedra, [2] papel, [3] tesoura')
# usuario escolhe um numero
usuario = int(input(': '))
# computador escolhe um numero entre 1 e 3 usando randint
computador = randint(1, 3)
print(computador)
if computador == 1:
    if usuario == 1:
        print('empate')
    elif usuario == 2:
        print('usuario ganhou')
    elif usuario == 3:
        print('computador ganhou')
    else:
        print('opcao invalida')
elif computador == 2:
        if usuario == 2:
            print('empate')
        elif usuario == 1:
            print('computador ganhou')
        elif usuario == 3:
            print('usuario ganhou')

elif computador == 3:
        if usuario == 3:
            print('empate')
        elif usuario == 1:
            print('usuario ganhou')
        elif usuario == 2:
            print('computador ganhou')
        else :
            print('opcao invalida')