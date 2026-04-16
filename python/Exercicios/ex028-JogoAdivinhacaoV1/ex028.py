import random

print('Pensando em um número entre 0 e 5...')

numero = int(input('Tente adivinhar qual o número escolhido: '))
lista = [0 , 1 , 2 , 3 , 4 , 5]
nescolhido = random.choice(lista)

print('Eu pensei em {}, eai? Será q você acertou?'.format(nescolhido))
if numero == nescolhido:
    print('Uau! Você coneguiu acertar! Sorte grande em!')
else:
    print('Vish! Errou dessa vez, q azar!')
