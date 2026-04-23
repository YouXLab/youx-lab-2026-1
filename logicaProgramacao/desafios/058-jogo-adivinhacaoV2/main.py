from random import randint
print('Acabei de pensar em um número entre 0 e 10.\nSerá que consegue adivinhar qual foi?')
tent = 1
num = int(input('Qual é seu palpite? '))
sort = randint(1, 10)
while num != sort:
    tent += 1
    if num > sort:
        num = int(input('Menor... Tente novamente: '))
    elif num < sort:
        num = int(input('Maior... Tente novamente: '))
print(f'Parabéns! Você acertou com {tent} tentativas.')