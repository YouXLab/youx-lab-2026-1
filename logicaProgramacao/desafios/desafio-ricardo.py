def chutar(palavra, chute):
    if chute in palavra:
        for i, value in enumerate(palavra):
            if chute == value:
                tracos[i] = chute
    for n, valor in enumerate(tracos):
        print(f"{valor}", end=" ")
    print()


palavra = "teste"
letrasPalavras = []
for i in range(0, len(palavra)):
    letrasPalavras.append(palavra[i])
tracos = []
for i in range(0, len(letrasPalavras)):
    tracos.append("__")
print("-="*25)
print("Jogo da forca, você tem 6 chances para adivinhar a palavra:")
vida = 0
tentativas = []
for n, valor in enumerate(tracos):
    print(f"{valor}", end=" ")
print()
while "__" in tracos and vida < 6:
    chute = str(input("Chute uma letra: ")).strip()[0]
    while chute in tracos:
        print("Letra já digitada, tente novamente")
        chute = str(input("Chute uma letra: ")).strip()[0]
    if chute in palavra:
        chutar(letrasPalavras, chute)
    elif chute not in palavra and chute not in tentativas:
        vida += 1
        print(f"Letra incorreta, restam {6 - vida} tentativas")
        tentativas.append(chute)
    elif chute not in palavra and chute in tentativas:
        print(f"Letra incorreta já digitada, restam {6 - vida} tentativas")
    if "__" not in tracos:
        print("Você adivinhou a palavra!")
        break
if "__" in tracos:
    print("Suas vidas esgotaram!")

