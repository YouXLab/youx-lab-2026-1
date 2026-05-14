from random import randint
cont=0
computador= randint(1,1000)
jogador= ' '
while True:
    opcao=int(input('escolha uma opcao [1]PAR [2]IMPAR:'))
    numero = int(input('digite um numero:'))
    par = numero % 2 == 0
    if numero % 2 == 0:
        jogador = numero
    else:
        jogador = numero
    if computador + numero == par:
        print('o jogador venceu!')
        cont+=1
    else:
        print('o jogador perdeu!')
        break
print(f'o jogador ganhou {cont} vezes')
print(f'{computador}')