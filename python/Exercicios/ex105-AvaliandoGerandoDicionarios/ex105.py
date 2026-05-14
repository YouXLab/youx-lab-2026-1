def notas(*nts, situacao = False):
    '''
    --> Função para analisar notas e situação de um aluno!
    :param nts: uma ou mais notas de um aluno!
    :param situacao: valor opcional, mostra a situação do aluno de acordo com a média!
    :return: dicionario com informações da situação da turma!
    '''
    dicionario = {}
    dicionario['total'] = len(nts)
    dicionario['maior'] = max(nts)
    dicionario['menor'] = min(nts)
    dicionario['média'] = sum(nts) / len(nts)
    if situacao is True:
        if dicionario['média'] >= 8:
            dicionario['situação'] = 'BOA'
        elif 6 <= dicionario['média'] < 8:
            dicionario['situação'] = 'RAZOÁVEL'
        elif 5.9 < dicionario['média'] <3:
            dicionario['situação'] = 'RUIM'
        else:
            dicionario['situação'] = 'PÉSSIMA'
    return dicionario


resposta = notas(5.5, 9.5, 10, 6.5, situacao=True)
print(resposta)
print('-='*43)
help(notas)