distancia = float(input('Qual a distância de sua viagem? '))
print(f"você está prestes a começar uma viagem de {distancia}Km. ")
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"E o preço da sua passagem será de {preco:.2f}")





