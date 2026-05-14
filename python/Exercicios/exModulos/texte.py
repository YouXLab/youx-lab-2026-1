from exModulos.UtilidadesCeV import moeda
from exModulos.UtilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 10, 5)
