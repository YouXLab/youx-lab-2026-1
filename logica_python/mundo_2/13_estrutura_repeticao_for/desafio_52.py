num = int(input('digite um numero: '))
cont = 0
for c in range (num, 0, -1):
    if num % c == 0:
        cont += 1

if cont == 2:
    print('primo')
else:
    print('num é')