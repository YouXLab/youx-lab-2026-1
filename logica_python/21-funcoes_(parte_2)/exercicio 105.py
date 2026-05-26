def notas(*n, sit=False):
    """
    Função para analisar e gerar um dicionário com várias notas de alunos.

    :param n: uma ou mais notas dos alunos (aceita múltiplos valores).
    :param sit: valor lógico (opcional) que indica se deve ou não adicionar a situação.
    :return: dicionário com quantidade, maior/menor nota, média e, opcionalmente, a situação.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'

    return r


# Programa Principal
resposta = notas(5.5, 9.5, 8.5, sit=True)
print(resposta)

