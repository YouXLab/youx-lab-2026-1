n =float(input('Qual é o salário do funcionário? R$'))
novo = n + (n * 15 / 100)
print('Um funcionário que ganhava R${}, com desconto de 15% de aumento, passa a receber R${}'.format(n, novo))