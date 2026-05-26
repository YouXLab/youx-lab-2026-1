from operator import itemgetter
from random import randint
from time import sleep
sleep(1)
print("==="*30)
print("JOGO DOS DADOS...")
print("==="*30)
sleep(2)
print("==="*30)
print("ROLANDO DADOS...")
print("==="*30)
sleep(1)
jogo = {"1° JOGADOR":randint(1,6),
"2° JOGADOR":randint(1,6),
"3° JOGADOR":randint(1,6),
"4° JOGADOR":randint(1,6)}
sleep(1)
rankDosMelhores = list()
print("==="*30)
print("OS VALORES SORTEADOS FORAM...")
print("==="*30)
sleep(2)
print(jogo)
sleep(2)
for keys, valor in jogo.items():
    print(f"{keys} tirou {valor} no Dado...")
    sleep(1)
rankDosMelhores = sorted(jogo.items(), key=itemgetter(1), reverse = True)#jogos.intens() == TUDO, Key=itemgetter == coletor de itens e reverse = True == inverte tudo
print("==="*30)
print('RANKING DOS MELHORES/MAIS SORTUDOS...')
print("==="*30)
sleep(2)
for item,valor in enumerate(rankDosMelhores):
    print(f"{item + 1}° lugar: ficou o {valor[0]} com {valor[1]}")
    sleep(1)
sleep(5)
print("")
print("É ISSO...")
print(";)")











