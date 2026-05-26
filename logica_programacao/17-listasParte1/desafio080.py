#Exercício Python 080: Crie um programa onde o usuário
# possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final,
# mostre a lista ordenada na tela.

import bisect
numeros = []
for inteiro in range(5):
    numeral = int(input('Digite um número: '))
    bisect.insort(numeros, numeral)
    print(f'Número {numeral} incluido na posição {numeros.index(numeral)}')
print(f'Numbers digitados: {numeros}')






















#qual a diferença de usar esse módulo e usar um sort? pra fim de exercício, a intenção era não usar de maneira automatizada.
# A diferença é que bisect.insort já insere de forma ordenada, o sort precisa da lista com elementos primeiro pra depois ordenar (é uma etapa a mais). Pode não ser a intenção do exercício, mas tem gente (como eu) que gosta de aprender além do exercício uma forma de automatizar. O intuito do meu comentário é a quem interessar, particularmente eu faço o exercício e, depois, pesquiso como eu poderia ter feito ele de uma maneira melhor 🙂




















