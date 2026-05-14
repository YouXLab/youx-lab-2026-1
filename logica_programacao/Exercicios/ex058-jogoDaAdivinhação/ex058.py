from random import  randint
computador = randint(0 ,10)
jogador = ''
palpite = 0
while jogador != computador:
    palpite += 1
    jogador = int(input("Digite outro numero: "))
    print ("voce errou, tente novamente ")
print(F"Voce acertou  \n foram necessarios {palpite} palpites  ")

