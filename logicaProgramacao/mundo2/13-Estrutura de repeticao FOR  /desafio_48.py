soma = 0
cont = 0
for con in range (1 ,501, 2):
    if con % 3 == 0:
     cont = cont + 1
     soma = soma + con
print('A soma de todos {} valores solicitados e {}'.format(cont, soma))