quantidade_de_opcoes = 0
escolha = "x"
while escolha != "Q":
    print('[1]PÉSSIMO\n[2]RUIM\n[3]OK\n[4]BOM\n[5]EXELENTE')
    print('[Q] PARA SAIR/ENCERRAR O PROGRAMA.')
    escolha = str(input('ESCOLHA UMA OPÇÃO:')).upper().strip()
    if escolha == '1' or escolha == '2' or escolha == '3' or escolha == '4' or escolha == '5':
        motivo = str(input('QUAL O MOTIVO DA SUA OPÇÃO?:'))
        quantidade_de_opcoes = quantidade_de_opcoes + 1
    elif escolha == 'Q':
        print('PROGRAMA FINALIZADO')
    else:
        print('OPÇÃO INVÁLIDA')


print(f'VOCÊ ESCOLHEU {quantidade_de_opcoes}')
