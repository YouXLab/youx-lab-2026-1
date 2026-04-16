salario = float(input('Qual seu salário atual? R$'))

if (salario > 1250.00):
    aumento = (salario * 10)/100
    print('Você recebeu um aumento de 10%, seu salário atual é R${}'.format(aumento + salario))
else:
    aumento = (salario * 15)/100
    print('Você recebeu um aumento de 15%, seu salário atual é R${}'.format(aumento + salario))