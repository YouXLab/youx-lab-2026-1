import moeda

dinheiro = float(input("Qual o valor em R$?:"))
print(f"A METADE DE R${dinheiro} É R${moeda.metade(dinheiro)}")
print(f"O DOBRO DE R${dinheiro} É R${moeda.dobro(dinheiro)}")
print(f"AUMENTANDO 20% O VALOR DE {dinheiro} PASSARÁ A SER {moeda.aumentar(dinheiro, 20)}")
print(f"DIMINUINDO 30% O VALOR DE {dinheiro} PASSARÁ A SER {moeda.diminuir(dinheiro, 30)}")







