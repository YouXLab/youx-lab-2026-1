def notas(*n, situacao=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita múltiplos valores).
    :param situacao: valor booleano (opcional) que indica se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r
resp = notas(5.5, 9.5, 8.0, 7.0, situacao=True)
print(resp)
help(notas)