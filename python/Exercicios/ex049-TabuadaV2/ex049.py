numero = int(input('Digite o número para a tabuada: '))

for tabuada in range(1, 11):
    print('{} * {:2} = {}'.format(numero, tabuada, numero*tabuada))
