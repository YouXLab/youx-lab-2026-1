valores = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Ultimo numero: ')))

print(f'Você digitou os valores: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O número 3 apareceu na posição {valores.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares foram ',end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')