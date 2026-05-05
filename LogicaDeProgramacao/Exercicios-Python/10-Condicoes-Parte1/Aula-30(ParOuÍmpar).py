N1 = float(str(input('N1: ')))
N2 = float(str(N1)[-3])
print(N2)
if N2 in [0,2,4,6,8]:
    print('par')
else:
    print('impar')