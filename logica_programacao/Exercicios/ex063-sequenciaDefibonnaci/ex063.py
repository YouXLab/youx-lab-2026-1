sequencia = int(input("Quantos numeros da sequencia firbonaccu voce quer mostrar/"))
c = 0
segundo = c
proximo = 1
print('0', end=' > ')
while c <= sequencia-2:
    print( proximo ,end=' > ')
    c +=1
    proximo += segundo
    segundo = proximo - segundo
print('fim')