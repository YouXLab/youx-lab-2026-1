peso = float(input('Qual seu peso? (kg'))
altura = float(input('Qual sua altura? (m)'))
IMC = peso / (altura ** 2)
print(f'O IMC dessa pessoa e {IMC}')
if IMC < 18.5:
    print('VOCE ESTA ABAIXO DO PESO!')
elif 18.5 <= IMC < 25:
    print('PARABENS! Seu peso esta ideal.')
elif 25 <= IMC < 30:
    print('Voce esta em SOBREPESO!')
elif 30 <= IMC < 40:
    print('Voce esta em obesidade! CUIDADO')
elif IMC > 40:
    print('Voce esta em OBESIDADE MORBIDA! Se cuide!')
