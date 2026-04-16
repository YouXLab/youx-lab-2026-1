N1 = float(input('Escreva a largura da parede: '))
N2 = float(input('Escreva a altura da parede: '))

N3 = N1 * N2
N4 = N3 / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(N1, N2, N3))

print('Para pintar essa parede, você precisará de {}l de tinta.'.format(N4))