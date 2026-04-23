soma = 0
cont = 0

termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo10 = (termo1 + (10 - 1) * razao)
for pa in range(termo1, termo10 + razao, razao):
    print('{} '.format(pa), end='→ ')
print('ACABOU')

