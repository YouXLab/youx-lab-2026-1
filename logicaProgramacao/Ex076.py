lista = ('Arroz',16.00,'Batata',3.50,'Verduras',3.00,'Carne',20.00,'Leite',5.00,'Chocolate',7.00,'Oleo',6.50,'Suco',4.50,'Frutas',3.75,'Feijao',13.00,'Acucar',5.00,
    'Champagne',60.00,'Bala',0.50)
print(' ---=---TABELA DE PRECOS---=--- ')
for i in range (0,len(lista),2):
    nome = lista[i]
    preco = lista[i+1]
    print(f" {nome:<12} | {preco:>12} R$")


