from random import randint
sorteio = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5) )
for cont in sorteio:
    print(f'Os valores sorteados foram: {sorteio[cont]}')