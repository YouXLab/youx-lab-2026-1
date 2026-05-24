def notas(*n):
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)

    return dados

print(notas(5, 7, 9))


# com situacao:
def notas(*n):
    media = sum(n) / len(n)

    if media >= 7:
        sit = 'Boa'
    elif media >= 5:
        sit = 'Razoável'
    else:
        sit = 'Ruim'

    return {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'media': media,
        'situação': sit
    }

print(notas(5, 7, 9))