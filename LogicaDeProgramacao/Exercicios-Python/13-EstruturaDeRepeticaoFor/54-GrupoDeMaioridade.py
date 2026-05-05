from datetime import date
T = 0
t = 0
N1 = date.today().year
for c in range(1,8):
    N2 = int(input(f'Idade da pessoa {c}: '))
    N3 = N1 - N2
    if N3 >= 18:
     T += 1
    else:
     t += 1
print(f'Teve {T} pessoas maiores de idade e {t} pessoas menores de idade.')