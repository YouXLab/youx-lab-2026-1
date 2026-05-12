def notas(*list, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param list: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com varias informações sobre a turma.
    """
    dados = {}
    dados['total'] = len(list)
    maior = 0
    menor = 0
    soma = 0
    for n in list:
        if n == 0 :
            maior = n
        elif n > maior:
            maior = n
    dados['maior'] = maior
    for n in list:
        if menor == 0:
            menor = n
        elif n < menor:
            menor = n
    dados['menor'] = menor
    for n in list:
        soma += n
    dados['media'] = soma / len(list)
    if sit == True:
        if dados['media'] < 7:
            dados['situação'] = 'Ruim'
        else:
            dados['situação'] = 'Boa'

    print(dados)

notas(5, 8, 10, 7, sit=True)
help(notas)