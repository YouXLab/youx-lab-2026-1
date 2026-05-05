velocidade =float(input('qual e atual velocidade do seu carro?'))
if velocidade > 80:
    print('MULTADO! você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('você deve pagar uma multa de {:.2f}'.format(multa))
print('tenha um bom dia! dirija com segurança ')
