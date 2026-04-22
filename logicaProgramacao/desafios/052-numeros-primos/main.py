divisiveis = []
num = int(input('Digite um número: '));
tot = 0
for c in range(1, num + 1):
    divisivel = num % c == 0
    if divisivel:
        divisiveis.append(c)
        tot += 1
print(f'\nO número {num} foi divisível {tot} vezes, os números são {divisiveis}');
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')