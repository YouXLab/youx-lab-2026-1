from random import randint
lista = list()
jogos = list()
print('-'*30)
print('      JOGUE NA MEGA SENA      ')
print('-'*30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-='*3, f' SORTEANDO {quantidade} JOGOS ', '-='*3)
for indice, l in enumerate(jogos):
    print(f'Jogo {indice+1}: {l}')