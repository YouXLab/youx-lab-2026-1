valor =int(input('valor da casa: '))
salario =int(input('salario do comprador: '))
emprestimo =int(input('quantos anos de financiamento? '))
salario30p = salario * 0.3
meses = emprestimo * 12
parcelaMensal = valor / meses
if parcelaMensal <= salario30p:
    print('emprestimo aceito')
else:
    print('emprestimo negado')
