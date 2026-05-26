import ex108
preco = int(input('Digite um preço: R$'))
print(f'Aumentando em 10%, temos {ex108.moeda(ex108.aumentar(preco, 10))}')
print(f'Reduzindo em 10%, temos {ex108.moeda(ex108.reduzir(preco, 10))}')
print(f'O dobro de {ex108.moeda(preco)} é {ex108.moeda(ex108.dobro(preco))}')
print(f'A metade de {ex108.moeda(preco)} é {ex108.moeda(ex108.metade(preco))}')