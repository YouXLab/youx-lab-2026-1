N1 = float(input('Digite o primeiro numero:'))
N2 = float(input('Digite o segundo numero:'))

if N1 > N2:
    print('O primeiro numero é maior')

elif N1 < N2:
    print('O segundo numero é maior')
elif N1 == N2:
    print('Os dois possuem o mesmo valor')
else:
    print('ERRO')