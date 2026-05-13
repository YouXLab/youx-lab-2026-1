def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <16:
        return f'com {idade} anos não vota!'
    elif 16 <= idade <18 or idade > 65:
        return f'com {idade} anos é opcional votar!'
    else:
        return f'com {idade} anos é obrigatório votar!'


nascimento = int(input('Qual sua data de nascimento: '))
print(voto(nascimento))