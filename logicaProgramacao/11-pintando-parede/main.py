larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
area = larg * alt 
print('sua parede tem a dimensao de {}x{} e sua area é de {}m²'.format(larg, alt, area))
tinta = area /2
print('para pintar essa parede, voce precisara de {}l de tinta.'.format(tinta))