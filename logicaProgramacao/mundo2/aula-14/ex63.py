# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma Sequência de Fibonacci.
#
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
numero = int(input('Digite a posicao na sequencia de fibonacci que deseja saber o valor: '))
ultimo_termo = 1
penultimo_termo = 0
for n in range(0, numero):
    if n == 0:
        print('0', end='')
    elif n == 1:
        print('1', end='')
    else:
        termo_atual = ultimo_termo + penultimo_termo
        print(termo_atual, end='')
        penultimo_termo = ultimo_termo
        ultimo_termo = termo_atual

    if n != numero - 1:
        print(' - ', end='')