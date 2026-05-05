from datetime import date
N1 = date.today().year
N2 = int(input('Qual sua data de nascimento? '))
N3 = N1 - N2
N4 = 18 - N3
N5 = N3 - 18
if N3 == 18 :
    print('Você tem a idade certa para fazer o alistamento')
elif N3 > 18:
    print(f'Você precisava ir para o alistamento á {N5} anos atras')
elif N3 < 18 :
    print(f'Falta {N4} anos para seu alistamento')
else:
    print('ERRO')