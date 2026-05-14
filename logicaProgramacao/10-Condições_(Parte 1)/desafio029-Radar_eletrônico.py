carro =int(input('Qual a velocidade atual do carro?'))
valor = ((80 - carro) * -1) * 7
if carro >=80:
    print(f'multado, voce ultrapassou a velocidade permitida 80 Km/h, voce deve pagar R$ {valor},00 de multa')
else: carro < 80
print('voce nao foi multado')
