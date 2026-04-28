Salario = float(input('Digite o valor do salario: '))
if Salario <= 1250:
    aumento = Salario + Salario * 15 / 100
if Salario >= 1250:
    aumento = Salario + Salario * 10 / 100
print(f'O valor do salario que era {Salario}R$ com o aumento foi pra {aumento}R$')
