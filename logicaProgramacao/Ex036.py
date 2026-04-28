Casa = float(input('Digite o valor da casa: '))
Salario = float(input('Digite o valor do salario: '))
Anos = float(input('Em Quantos anos voce pretende pagar: '))
Meses = Anos * 12
Prestacao = Casa / Meses
Limite = Salario * 30 / 100
print('Para pagar uma casa de {} em {} anos a prestacao sera de {:.2f}'.format(Casa, Anos, Prestacao))
if Limite >= Prestacao:
    print('Seu emprestimo foi aprovado,pois a prestacao nao ultrapassa 30% do salario')
else:
    print('Seu emprestimo para comprar uma casa foi negado pois ultrapassou 30% do salario')
