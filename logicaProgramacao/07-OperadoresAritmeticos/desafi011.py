#Faça  um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessario para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m

larg = float(input('largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg* alt
print('Sua parede tem a dimensao de {}x{} e sua area é de {}m .'.format(larg, alt,area))
tinta = area / 2
print('Para pintar essa parede, voce precisara de {}l de tinta.'.format(tinta))
 
