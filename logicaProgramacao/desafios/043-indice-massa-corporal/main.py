p = float(input('Qual é seu peso? (Kg) '));
m = float(input('Qual é sua altura? (m) '));
imc = p / (m ** 2);
print(f'O IMC dessa pessoa é de {imc:.1f}');
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.');
elif 18.5 < imc <= 25:
    print('Parabéns, você está no PESO IDEAL.');
elif 25 < imc <= 30:
    print('Você está com SOBREPESO.');
elif 30 < imc <= 40:
    print('Você está com OBESIDADE.');
else:
    print('Você está com OBESIDADE MÓRBIDA.');