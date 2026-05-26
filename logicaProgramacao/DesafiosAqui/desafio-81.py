"""Exercício Python 081: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
from tokenize import endpats

valores = []
resposta = None
numero = 0
while resposta != 'N':
    numero = int(input('Digite um número: '))
    valores.append(numero)
    resp = str(input('Quer continuar? [S/N] '))
    resposta=resp.upper()
valores.sort(reverse=True)
print('≃'*30)
if 5 in valores:
    print('Tem o número 5!')
else:
    print('Não tem o número 5!')
print(f'Tem {len(valores)} elementos.')
print(f"""Os números digitados foram:
{valores}""")
