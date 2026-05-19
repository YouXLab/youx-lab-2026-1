#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com voce.


from random import randint
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0,2)
print("Suas opçoẽs são:   [0]PEDRA   [1]PAPEL   [2]TESOURA")
jogador = int(input("Qual é a sua jogada?"))

if (jogador == 0):
    if (computador == 0):
        print("EMPATE")
    elif (computador == 1):
        print("COMPUTADOR GANHOU")
    elif (computador == 2):
        print("JOGADOR GANHOU")

elif (jogador == 1):
    if (computador == 0):
        print("JOGADOR GANHOU")
    elif (computador == 1):
        print("EMPATE")
    elif (computador == 2):
        print("COMPUTADOR GANHOU")

elif (jogador == 2):
    if (computador == 0):
        print("COMPUTADOR GANHOU")
    elif (computador == 1):
        print("JOGADOR GANHOU")
    elif (computador == 2):
        print("EMPATE")
else:
    print("digitou opção inválida")


print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
