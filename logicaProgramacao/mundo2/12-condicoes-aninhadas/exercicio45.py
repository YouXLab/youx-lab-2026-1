import random
import time
from random import choice
from time import sleep
print("VAMOS JOGAR JOKENPO!! ESCOLHA UMA DAS OPÇOES ABAIXO \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA")
mao_jogador = int(input(""))
lista = 1 , 2 , 3
print(" JO "
      "\n KEN "
      "\n PO!!! ")
resultado = choice(lista)
if resultado == mao_jogador:
     print("Empate")
elif resultado == 1 and mao_jogador == 2 or resultado == 2 and mao_jogador == 3 or resultado == 3 and mao_jogador == 1:
     print("Voce ganhou")
else:
    print("Voce perdeu ")


