def area(larg, comp):
    a = larg * comp
    print(f'a área de um terreno {larg}*{comp} é de {a}m².')
print('Controles de terreno')
l = float(input('LARGURA (m): '))
c = float(input(' COMPRIMENTO (m): '))
area(l, c)