#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
# jogos serão gerados  e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
# lista composta.

from random import randint
from time import sleep

lista= list()
jogo=list()
quantia = int(input('Quantos jogos vc quer fazer:'))
total = 1
while total <= quantia:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 5, f'Sorteando {quantia} Jogos', '-=' * 5)
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    sleep(1)