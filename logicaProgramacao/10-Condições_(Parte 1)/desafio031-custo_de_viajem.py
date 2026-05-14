custo =float(input('Qual e a distancia da sua viajem? '))
print(f'voce esta prestes a comecar a viajem a {custo} Km')
if custo <= 200:
    preco = custo * 0.50
else:
    preco = custo * 0.45
print(f'e o preco sera de {preco}')