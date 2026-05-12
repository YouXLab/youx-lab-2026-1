palavras = ('Abracadabra','Filmes','Comidas','Animais','Cachorro','Estrela','Planeta','Espaco','Teste','Batore','Escrita')
# u == unidade de palavra
print('------VOGAIS------')
print('-=-' * 10)
for u in palavras:
    print(f'\nNa palavra {u.upper()} temos ', end='')
    for letra in u:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')


