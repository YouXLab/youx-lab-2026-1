distancia =int(input('Qual é a distância da sua viagem?:'))
if distancia <200:
    preco = distancia * 0.50
else:
   preco = distancia * 0.45
print(f'Sua viagem de {distancia}km:')
print(f'custará: R${preco:.2f} ' )





