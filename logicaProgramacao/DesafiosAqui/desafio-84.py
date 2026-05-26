"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
resp = None
maior = float('-inf')
menor = float('inf')
nome_maior = None
nome_menor = None
nm = []
ps = []
contador = 0
while resp != 'N':
    nome = str(input('Nome: '))
    nm.append(nome)
    peso = float(input('Peso: '))
    ps.append(peso)
    ps_maior = sorted(ps)
    if maior <peso:
        maior =  peso
        ps_maior = contador
    if menor >peso:
        menor = peso
        ps_menor = contador
    resposta = str(input('Quer continuar?[S/N] '))
    resp = resposta.upper().strip()
    contador += 1
    print(nm)
    print(ps)
    if resp != 'S':
        resp = 'N'
    print(ps_maior*1)
print(f'O maior peso foi {maior} kg')
print(f'O menor peso foi {menor} kg')