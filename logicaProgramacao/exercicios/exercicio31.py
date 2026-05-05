distancia =float(input('qual é a sua distância?'))
print('você esta prestes a começar uma viagem de {}km'.format(distancia))
preco =  distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(' e o preço da sua passagem sera de R$ {:.2f}'.format(preco))
