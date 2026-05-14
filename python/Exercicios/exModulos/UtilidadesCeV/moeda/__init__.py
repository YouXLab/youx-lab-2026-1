def aumentar(preco=0, taxa=0, formato=False):
    resultado = preco + (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formato=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def dobro(preco=0, formato=False):
    resultado = preco * 2
    return resultado if formato is False else moeda(resultado)


def metade(preco=0, formato=False):
    resultado = preco / 2
    return resultado if formato is False else moeda(resultado)


def moeda(preco=0, moeda='R$', formato=False):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaaum=10, taxadim=5):
    print('-' * 33)
    print('RESUMO DO VALOR'.center(33))
    print('-' * 33)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'Dobro do preço: \t\t{dobro(preco, True)}')
    print(f'Metade do preço: \t\t{metade(preco, True)}')
    print(f'Com {taxaaum}% de aumento: \t{aumentar(preco, taxaaum, True)}')
    print(f'Com {taxadim}% de redução: \t\t{diminuir(preco, taxadim, True)}')
    print('-' * 33)
