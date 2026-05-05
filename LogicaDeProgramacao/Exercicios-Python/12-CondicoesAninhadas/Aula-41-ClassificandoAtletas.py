from datetime import date
N1 = int(input('Ano de nascimento: '))
N2 = date.today().year
N3 = N2 - N1
if N3 <= 9:
    print('MIRIM')
elif N3 <= 14:
    print('INFANTIL')
elif N3 <= 19:
    print('JÚNIOR')
elif N3 <= 25:
    print('SÊNIOR')
elif N3 > 25:
    print('MASTER')
else:
    print('ERRO')