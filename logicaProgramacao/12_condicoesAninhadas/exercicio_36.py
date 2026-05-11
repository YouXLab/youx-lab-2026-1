casa=float(input('qual o valor da casa? :'))
salario=float(input('qual o salario do comprador? :'))
anosPagamento=int(input('em quantos anos ele vai pagar? :'))
tempoMeses = casa / anosPagamento * 12
parcela= salario * 30 / 100
print(f'para pagar uma casa de {casa} em {anosPagamento}')
print((f'a prestacao sera de {tempoMeses}'))
if tempoMeses <= parcela:
    print('emprestimo aceito')
else:
    print('emprestimo negado')
