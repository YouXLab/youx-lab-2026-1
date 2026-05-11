velocidade= int(input('a velocidade do carro é :'))
if velocidade > 80:
    print('voce foi multado por ultrapassar 80km/h')
    multa= (velocidade-80)* 7
    print(f'voce deve pagar uma multa de R${multa}')
else:
    print('bom dia, dirija com segurança')