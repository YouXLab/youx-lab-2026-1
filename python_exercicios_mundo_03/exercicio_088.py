#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


from random import randint
from time import sleep
lista = []
jogo = []
total = 1
quantidade = int(input("quantos jogos vc quer sortear? "))
while total <= quantidade:
    contador = 0
    while contador < 6:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total += 1
print("SORTEANDO")
for i in range(len(jogo)):
    print(f"jogo{i + 1}:{jogo[i]}")
    sleep(1)
