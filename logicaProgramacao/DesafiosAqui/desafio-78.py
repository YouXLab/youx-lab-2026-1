'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em
uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
'''
from operator import index
maior = float("-inf")
menor = float("inf")
pos_maior = None
pos_menor = None
valores = list ()
for n in range(0,5):
    valor_atual = int(input(f'Digite um valor para a posição {n}: '))
    valores.append(valor_atual)
    if maior <valor_atual:
        maior = valor_atual
        pos_maior = n
    if menor >valor_atual:
        menor =  valor_atual
        pos_menor = n
print('-=' * 20)
#for c,valor in enumerate(valores):
 #   print(f'Na posição {c} tem o valor {valor}!')
n=len(valores)
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {maior} na posições... {pos_maior}')

print(f'O menor valor digitado foi {menor} na posição... {pos_menor}')