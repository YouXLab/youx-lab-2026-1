N1 = int(input('Digite o primeiro termo: '))
N2 = int(input('Digite sua razão: '))
P1 = N1
P2 = N2
P3 = (P2 * 9) + P1
while P1 != P3:
    print(f'{P1} ',end='')
    print(' ' if P1 == P3 else ' -> ',end='')
    P1 += P2
print(P3,'Fim.')