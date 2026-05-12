import random
n = tuple(random.randint(1,10) for _ in range(5))
print(f'Os valores sorteados foram {n}')
print('-=-' * 10)
print(f'O Maior Numero foi: {max(n)}')
print('-=-' * 10)
print(f'O Menor Numero foi: {min(n)}')
print('-=-' * 10)