N1 = 0
N2 = 0
cont = 0
while N1 != 999:
    print('Digite [999] para parar')
    N1 = int(input('Digite um valor: '))
    cont = cont + 1
    N2 = N1 + N2
N2 = N2 - 999
cont = cont - 1
print(cont , N2)
