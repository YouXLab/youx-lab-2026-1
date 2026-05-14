#r = 'S'
#while r == 'S':
#    n=int(input('digite um valor:'))
   # r=str(input('quer continuar? [S/N] ')).upper()
#print('fim')

par=impar=0
n=1
while n !=0:
    n=int(input('digite um valor:'))
    if n != 0:
      if n % 2 == 0:
        par += 1
      else:
         impar += 1
print(f'voce digitou {par} numeros pares e {impar} numeros impar')