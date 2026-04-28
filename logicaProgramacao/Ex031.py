Viagem = float(input('Qual a distancia da sua viagem? '))
print(f'Voce esta prestes a inicar uma viagem de {Viagem:.2f} km.')
if Viagem <= 200:
    preco = Calculo = Viagem * 0.50
else:
    preco = Calculo = Viagem * 0.45
print(f'O preco da sua viagem vai ser de {preco:.2f} R$')