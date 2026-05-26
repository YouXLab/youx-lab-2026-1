#Exercicio 105. Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:

def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    resumo_notas = {}
    if len(n) == 0:
        return 'Você deve informar ao menos uma nota!'
    resumo_notas['Quantidade de notas'] = len(n)
    resumo_notas['Maior nota'] = max(n)
    resumo_notas['Menor nota'] = min(n)
    media = sum(n) / len(n)
    resumo_notas['Média da turma'] = media
    if sit:
        if media <= 5:
            resumo_notas['Situação'] = 'RUIM'
        elif media <= 7:
            resumo_notas['Situação'] = 'RAZOÁVEL'
        elif media <= 9:
            resumo_notas['Situação'] = 'BOA'
        else:
            resumo_notas['Situação'] = 'EXCELENTE'
    return resumo_notas
# Teste
resposta = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resposta)