N1 = int(input('Digite um numero [digite 0 para parar]: '))
N2 = 0
cont = 0
while N1 != 0:
    N1 = int(input('Digite um numero [digite 0 para parar]: '))
    cont = cont + 1
    N2 = N2 + N1
print(N2)