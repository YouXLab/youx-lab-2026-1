import random
print('Pensando em um número entre 0 e 5. Tente adivinhar...');
n1 = random.randint(0, 10)
print(n1);
n = int(input('Em que número eu pensei? '));
print('PROCESSANDO...');
if n == n1:
    print('PARABÉNS! Você acertou!');
else:
    print('Você errou!');
