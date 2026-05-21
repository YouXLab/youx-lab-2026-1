expressao_valida = False
while expressao_valida == False:
    expressao = input('Digite a expressão: ')
    pilha = []
    erro = False
    for simb in expressao:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                erro = True
    if len(pilha) == 0 and erro == False:
        print('Sua expressão está válida!')
        expressao_valida = True
    else:
        print('Sua expressão está errada! Tente novamente.')