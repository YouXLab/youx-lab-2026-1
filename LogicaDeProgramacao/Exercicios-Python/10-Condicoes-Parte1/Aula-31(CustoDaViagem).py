N1 = float(input('Qual a distancia da viagem? '))
N2 = (N1 * 0.5)
N3 = (N1 * 0.45)
print(f'Você esta prestes a começar uma viagem de {N1}KM')
if N1 <= 200:
    print(f'Você vai pagar R${N2}')
else:
    print(f'Você vai pagar R${N3}')