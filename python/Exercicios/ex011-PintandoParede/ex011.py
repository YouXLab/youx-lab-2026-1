al = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
ar = (al * l)
t= ar / 2

print('As dimensões da parede são {} x {}, e sua área é de {:.2f}m²'.format(al, l, ar))
print('Para a pintura, serão necessários {:.2f}L de tinta.'.format(t))