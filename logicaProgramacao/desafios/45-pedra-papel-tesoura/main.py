import random;
print("Suas opções:\n1 - Pedra\n2 - Papel\n3 - Tesoura");
j = int(input("Qual sua jogada?: "));
r = random.randint(1, 3);
if j == 1:
    if r == 2:
        print("Eu escolhi Papel Você perdeu!");
    elif r == 1:
        print("Eu escolhi Pedra O jogo empatou!");
    elif r == 3:
        print("Eu escolhi Tesoura Você ganhou!");


elif j == 2:
    if r == 2:
        print("Eu escolhi Papel O jogo empatou!");
    elif r == 1:
        print("Eu escolhi Pedra Você ganhou!");
    elif r == 3:
        print("Eu escolhi Tesoura Você perdeu!");

elif j == 3:
    if r == 2:
        print("Eu escolhi Papel Você ganhou!");
    elif r == 1:
        print("Eu escolhi Pedra Você perdeu!");
    elif r == 3:
        print("Eu escolhi Tesoura O jogo empatou!");