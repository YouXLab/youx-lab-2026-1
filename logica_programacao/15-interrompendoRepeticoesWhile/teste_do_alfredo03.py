#Fazer sem while True,break
print('ESCOLHA UMA OPÇÃO:')
print('[1]PÉSSIMO\n[2]RUIM\n[3]OK\n[4]BOM\n[5]EXELENTE')
print('[Q] PARA SAIR/ENCERRAR O PROGRAMA.')
opcao_escolhida = int(input('ANALISANDO,QUAL OPÇÃO VOCÊ ESCOLHEU?:'))
while opcao_escolhida == '1' or '2' or '3' or '4' or '5':
    print('VOCÊ ESCOLHEU UMA OPÇÃO,PARABÉNS EU ACHO...')
    opcao_escolhida = int(input('ESCOLHA OUTRA:'))
    if opcao_escolhida == 'Q':
        print('ACABOU')
print('FIM')













