palavras = ('Lagrimas','Flamingos','Bluesman','Inimigos',
            'QVVFA')
for p in palavras:
    print(f'\n  Na palavra {p:.<12}temos = ',end= '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')