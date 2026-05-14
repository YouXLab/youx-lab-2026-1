n1 =float(input('Largura da parede: '))
n2 =float(input('Altura da parede:'))
print('Sua parede tem dimensao de {}x{} e sua área é {}m²'.format(n1, n2, n1*n2))
n3 = (n1*n2) / 2
print('Para pintar {}m² de parede , você precisará de {} litros de tinta'.format(n1*n2, n3))