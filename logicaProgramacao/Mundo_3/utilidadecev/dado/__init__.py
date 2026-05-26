def aumentar(v, p, formato=False):
    preco = v + (v * p/100)
    if formato == True:
        preco = f'R${preco:.2f}'
    return preco

def reduzir(v, p, formato=False):
    preco = v - (v * p/100)
    if formato == True:
        preco = f'R${preco:.2f}'
    return preco

def dobro(v, formato=False):
    preco = v * 2
    if formato == True:
        preco = f'R${preco:.2f}'
    return preco

def metade(v,formato=False):
    preco = v / 2
    if formato == True:
        preco = f'R${preco:.2f}'
    return preco

def moeda(v):
    preco = f'R${v:.2f}'
    return preco

def resumo(v, a, r):
    print(f'{'Resumo do valor':^30}')
    print(f'Preço analizado:  R${v:.2f}')
    print(f'Dobro do preço:  R${v*2:.2f}')
    print(f'Metade do preço:  R${v/2:.2f}')
    print(f'{a}% de aumento:  R${v + (v*a/100):.2f}')
    print(f'{r}% de redução:  R${v - (v*r/100):.2f}')