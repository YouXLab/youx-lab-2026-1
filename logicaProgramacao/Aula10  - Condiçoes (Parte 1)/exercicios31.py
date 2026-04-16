#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("Digite a distancia em km da sua viagem: "))
if distancia >=200:
 preco_km = distancia * 0.45
 print(f"Voce pagara R${preco_km}")
else:
 preco_km = distancia * 0.50
 print(f"Voce pagara R${preco_km}")

