menor=0
maior=0
for c in range(1,6):
 peso=float(input('peso da pessoa:'))
 if c == 1:
     menor == peso
     maior == peso
else:
  if peso > maior:
    maior = peso
if peso < menor:
 menor = peso
print(f'o maior peso foi: {maior}')
print(f'o menor peso foi: {menor}')