N1 = float(input('Qual o salario do funcionario? R$'))
N2 = N1 * 1.10
N3 = N1 * 1.15
if N1 <= 1250:
    print(f'Quem ganhava {N1} passa a ganhas {N3} agora.')
else:
    print(f'Quem ganhava {N1} passa a ganhas {N2} agora.')