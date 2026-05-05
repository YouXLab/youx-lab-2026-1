N1 = float(input('Valor da casa: R$'))
N2 = float(input('Salario do comprador: R$'))
N3 = float(input('Quantos anos de financiamento? '))

N4 = N1 / (N3 * 12)
N5 = N2 * 0.30

if N4 > N5:
    print('Emprestimo negado')
else:
    print('Emprestimo aceito')