import moeda

dinheiro = float(input("Qual o valor em R$?: "))
print(f"A METADE DE R${moeda.moeda(dinheiro)} É R${moeda.moeda(moeda.metade(dinheiro))}")
print(f"O DOBRO DE R${moeda.moeda(dinheiro)} É R${moeda.moeda(moeda.dobro(dinheiro))}")
print(f"AUMENTANDO 20% O VALOR DE {dinheiro} PASSARÁ A SER {moeda.moeda(moeda.aumentar(dinheiro, 20))}")
print(f"DIMINUINDO 30% O VALOR DE {dinheiro} PASSARÁ A SER {moeda.moeda(moeda.diminuir(dinheiro, 30))}")











