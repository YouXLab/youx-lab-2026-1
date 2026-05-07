salário = float(input('qual é o salário do funcionario? R$'))
novo = salário + (salário * 15/ 100)
print('um funcionario que gamhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
