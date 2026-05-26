from random import randint
jogos = []
lista = []
quant = int(input('Quantos jogos você que sortear? '))
total = 1
while total <= quant:
    for pare in range(6):
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'≃'*8,'JOGOS SORTEADOS','≃'*6)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
print('≃'*31)