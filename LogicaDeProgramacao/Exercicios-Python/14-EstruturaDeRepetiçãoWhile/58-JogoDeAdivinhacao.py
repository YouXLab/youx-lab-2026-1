import random
print('Sou seu computador.')
print('Acabei de pensar em um numero entre 0 a 10')
N1 = random.randint(0,10)
A1 = int(input('Digite seu palpite: ').strip())
P1 = 1
while A1 != N1:
    if A1 < N1:
        A1 = int(input('O numero é superior a este, tente novamente: ').strip())
        P1 += 1
    elif A1 > N1:
        A1 = int(input('O numero é inferior a este, tente novamente: ').strip())
        P1 += 1

print(f'Acertou o numero {N1} com {P1} tentativas. Parabéns')