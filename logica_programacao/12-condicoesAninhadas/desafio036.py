valorDaCasa = float(input('Qual o valor da casa?:'))
salarioDoComprador = float(input('Qual o salário do comprador?:'))
anosDeFinanciamento = float(input('Quantos anos de financiamento?:'))
salario30p = salarioDoComprador * 0.3
meses = anosDeFinanciamento * 12
parcelaMensal = valorDaCasa / meses
if parcelaMensal <= salario30p:
    print('Parabéns você acaba de comprar uma casa MAAARAVILHOSA!!! AGORA FICARÁ POBRE!!!')
else:
    print('Seu pobre fudido, você não tem saldo suficiente,portanto NEGAMOS SEU EMPRESTIMO ;)')

#O QUE EU FIZ? 1° VARIAVEL É O VALOR DA CASA,2°SALARIO DO COMPRADOR,3°ANOS DO FINANCIAMENTO,4° VARIAVEL FOI 30% DO SALARIO: COMO CALCULAMOS? SALARIO DO COMPRADOR * 30% (QUE É IGUAL A 0.3),5° MESES COMO CALCULAMOS? ANOS DO FINANCIAMENTO * 12 (EX: 2 ANOS É IGUAL A 24 MESES),6° VARIAVEL:O VALOR DA PARCELA...FIZ O VALOR DA CASA / MESES (EX: CASA CUSTA 100 REAIS E SAO 2 PARCELAS OU SEJA 100/2=50.CONCLUSÃO: SE A PARCELA DA CASA FOR MAIOR QUE OS 30% DO SALARIO (EX: PARCELA DE 200 E 30% DO SALARIO = 100) É NEGADO!!! CASO OPOSTO É APROVADO (EX: PARCELA 200 E 30% DO SALARIO FOR 300) É APROVADO!




# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.






