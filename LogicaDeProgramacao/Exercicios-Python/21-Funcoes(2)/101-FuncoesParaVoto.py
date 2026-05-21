def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 16 >= idade:
        print(f'Com {idade} não vota.')
    elif idade > 16 and idade < 18 or idade > 65:
        print(f'Com {idade} voto opcional.')
    else:
        print(f'Com {idade} voto obrigatorio.')
nasc = int(input('Digite sua idade: '))
voto(nasc)