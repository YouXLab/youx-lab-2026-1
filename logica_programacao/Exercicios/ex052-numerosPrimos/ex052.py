numero = int(input('digite um numero:'))
total = 0
for c in range(1, numero + 1):
     if numero % c == 0:
         total += 1
if total == 2:
  print('é primo')
else:
 print('nao é primo')