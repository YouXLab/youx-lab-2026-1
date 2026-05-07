velocidade = float(input('qual é a velocidade atual de carro? '))
if velocidade > 80:
    print('MULTADO! vocẽ exedeu o limite permitindo que é de 80Kn/h')
    multa = velocidade * 7
    print('vocẽ deve pagar uma multa de R${:.2f}!'.format(multa))
print('tenha um bom dia! Dirira com segurança!')