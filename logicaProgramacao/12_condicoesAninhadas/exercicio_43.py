peso= float(input('qual seu peso? :'))
altura=float(input('qual sua altura? :'))
imc= peso / altura ** 2
print(f'seu imc é {imc}')
if imc <18.5:
    print('voce esta abaixo do peso')
elif 18.5 <= imc < 25:
    print('voce esta no peso ideal')
elif 25 <= imc < 30:
    print('voce está acima do peso')
elif 30 <= 40:
    print('voce esta com obesidade')
elif imc > 40:
    print('voce esta com obesidade morbida')

