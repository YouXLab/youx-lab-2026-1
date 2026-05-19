from random import randint
numero = (randint(1, 10)), (randint(1, 10)), (randint(1,10)), (randint(1,10)), (randint(1, 10))
print(f'os valores sorteados foram', end='')
for cont in numero:
    print(cont, end=' ')

print(f' \nO maior valor obtido foi {max(numero)}')
print(f'o menor valor obtido foi {min(numero)}')