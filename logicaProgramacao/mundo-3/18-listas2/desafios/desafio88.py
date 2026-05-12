import random
import time

print('='*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('='*30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []
jogo = []
total = 1
while total <= quantidade:
    contador = 0
    while True:
        numero = random.randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            contador += 1
        if contador >= 6:
            jogo.sort()
            lista.append(jogo[:])
            jogo.clear()
            total += 1
            break
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)