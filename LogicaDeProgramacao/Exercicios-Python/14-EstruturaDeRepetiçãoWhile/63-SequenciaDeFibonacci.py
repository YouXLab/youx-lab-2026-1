# from itertools import count
#
# N1 = int(input('Quantos termos você quer? '))
# P1 = N1
# P2 = 0
# P3 = 0
# P4 = 1
#cont = 0
# while P2 != P1:
#      print(P4)
#      P2 = P2 + 1
#      P3 = P3 + P4
#      P4 = P4 + P3
# print(P4)
N1 = int(input('Quantos termos você quer? '))
P1 = 0
P2 = 1
P3 = 0
cont = 0
while N1 > cont:
    print(P3 ,'->',end=' ')
    P1 = P2
    P2 = P3
    P3 = P1 + P2
    cont += 1
print('Fim.')