#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha (n, g):
    if len(n) == 0:
        print(f'O jogador <desconhecido> fez {g} gol(s) no campeonato.')
    else:
        print(f'O jogador {n} fez {g} gol(s) no campeonato.')
n = str(input('Nome do jogador: '))
g = input('Número de gols: ')
if not g:
    g = 0
else:
    g = int(g)
ficha(n, g)