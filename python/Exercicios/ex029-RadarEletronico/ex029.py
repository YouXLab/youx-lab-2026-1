import math

carro = int(input('Qual a velocidade atual do carro? '))

if carro > 80:
    print('MULTADO!! Voce excedeu o limite de 80Km/h')
    multa = (carro - 80) * 7
    print('Sua multa será de R${}!'.format(multa))
else:
    print('OK!! Dirija com segurança e tenha um bom dia!')
