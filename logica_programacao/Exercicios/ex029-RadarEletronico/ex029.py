velocidade = float(input('digite a velocidade do carro:'))
if velocidade > 80:
 print('voce foi multado')
 multa = (velocidade - 80) * 7
print(f'voce tem que pagar uma multa de {multa}')