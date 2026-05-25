from random import randint
lista= list()
quantidade=int(input('quantos jogos vc quer q eu sorteio?'))
jogos=[]
for i in range(quantidade):
    jogo =[]

    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    jogos.append(jogo[:])
for i, jogo in enumerate(jogo, start=1):
    print(f'jogo {i}: {jogo}')