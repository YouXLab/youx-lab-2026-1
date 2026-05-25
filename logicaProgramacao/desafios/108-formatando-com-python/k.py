from ex108 import *

preço = float(input('Digite seu preço: R$ '))

print(f'A metade de {moeda(preço)} é {moeda(metade(preço))}')
print(f'O dobro de {moeda(preço)} é {moeda(dobro(preço))}')
print(f'Aumentado 10%, temos {moeda(aumentar(preço, 10))}')