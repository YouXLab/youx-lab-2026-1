num=(int(input('digite um numero:')),
        int(input('digite outro numero:')),
        int(input('digite mais um numero:'),
        int(input('digite o ultimo numero:')))

print(f'voce digitou os valores {num}')
print(f'o valor 9 foi digitado {num.count(9)} vezes')
if 3 in num:
        print(f'o numero 3 aparece na {num.index(3)+1} posiçao')
else:
        print('nao foi digitado nenhum numero 3')
print(f"os valores pares digitados foram", end='')
for pares in num:
  if pares % 2 == 0:
      print(pares, end=' ')
