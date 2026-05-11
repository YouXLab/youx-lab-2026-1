from random import randint
computador = randint(0, 5)
escolha = int(input('em que numero o computador pensou? (de 0 a 5)'))

if escolha == computador:
    print("voce ganhou")
else :
    print(f"tente de novo, o computador escolheu {computador}! Você perdeu!")