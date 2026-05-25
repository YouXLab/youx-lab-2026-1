def area(larg, comp):
    a = larg * comp
    print(f'a area de um terreno {larg}x{comp} é de {a}m')
print('controle de terrenos ')
l=float(input('largura (m): '))
c= float(input('comprimento (m): '))
area(l, c)