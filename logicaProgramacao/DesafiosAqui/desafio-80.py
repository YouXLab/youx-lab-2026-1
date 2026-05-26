"""Exercício Python 080:
Crie um programa onde o usuário possa digitar
cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""
from operator import pos

lista = []
for c in range(0,5):
    numero = int(input('Digite um valor: '))
    if c == 0  or numero >lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado a posição {pos}')
                break
            pos += 1
print('≃'*30)
print(f'Os valores digitados foram {lista}')