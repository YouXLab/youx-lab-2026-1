#def fatorial(n):
 #   f=1
  #  for c in range(1,n+1):
   #     f *= c
   # return f
#def dobro(n):
 #   return  n * 2

#def triplo(n):
 #   return n * 3

#num=int(input('digite um valor: '))
#fat=fatorial(num)
#print((f'o fatorial de {num} é {fat}'))
#print(f'o dobro de {num} é {dobro(num)}')
#print(f'o triplo de {num} é {triplo(num)}')

from uteis import numeros
num= int(input('digite um valor: '))
fat =uteis.fatorial(num)
print(f'o fatorial de {num} é {fat}')
print((f'o dobro de {num} é {uteis.dobro(num)}'))
