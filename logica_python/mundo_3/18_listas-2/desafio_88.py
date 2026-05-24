import random
numeros=[]
jogos=[]
jogo=1
entrada=int(input("Quantas listas você vai querer:"))
print(f"=-=-=-=-=-=-=-=-=  SORTENDO {entrada} JOGOS  =-=-=-=-=-=-=-=-=")
for i in range(1,61):
    numeros.append(i)
for c in range(0,entrada):
    for escolhidos in range(0,6):
        escolhido=random.choice(numeros)
        jogos.append(escolhido)
        numeros.remove(escolhido)
        if escolhidos==5:
            print(f"Jogo {jogo}: {jogos}")
            print("")
            jogo+=1
            for apagar in range(0,6):
                jogos.pop()