def notas(*list, situacao=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param list: uma ou mais notas dos alunos (aceita várias).
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário sobre várias informações sobre a situação da turma.
    '''
    dados = {}
    dados['total'] = len(list)
    maior = 0
    menor = 0
    soma = 0
    for i in list:
        if i == 0:
            maior = i
        elif i > maior:
            maior = i
    dados['maior'] = maior
    for i in list:
        if menor == 0:
            menor = i
        elif i < menor:
            menor = i
    dados['menor'] = menor
    for i in list:
        soma += i
    dados['média'] = soma / len(list)
    if situacao == True:
        if dados['média'] < 7:
            situacao = 'RUIM'
        else:
            situacao = 'BOA'
        dados['situação'] = situacao
    return dados



resp = notas(2, 2, situacao=True)
print(resp)
help(notas)