from random import randint

print('Pensando em um número entre 0 e 10...')

tentativa = 1
numero = int(input('Tente adivinhar qual o número escolhido: '))
computador = randint(0, 10)
while numero != computador:
    tentativa += 1
    if numero > computador:
        numero = int(input('MENOR! mas tente denovo! '))
    elif numero < computador:
        numero = int(input('MAIOR! Mas tente nevamente!'))
print('Parabéns!! você acertou em {} tentativas!'.format(tentativa))