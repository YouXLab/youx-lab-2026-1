viagem= float(input('qual a distancia da viagem ?'))
print(f'voce esta começando uma viagem de {viagem}')
preco= viagem * 0.50 if viagem <= 200 else viagem * 0.45
print(f'o preço da sua passagem é R${preco}')