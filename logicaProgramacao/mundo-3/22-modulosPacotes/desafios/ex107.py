def aumentar(v, p):
    preco = v + (v * p/100)
    return preco

def reduzir(v, p):
    preco = v - (v * p/100)
    return preco

def dobro(v):
    preco = v * 2
    return preco

def metade(v):
    preco = v / 2
    return preco

def moeda(v):
    preco = f'R${v:.2f}'
    return preco