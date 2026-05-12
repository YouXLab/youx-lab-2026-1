def area(comp, larg):
    area = comp*larg
    print(f'A área de um terreno {comp}x{larg} é de {area}')
print(' CONTROLE DE TERRENOS ')
print('-='*11)
comp = float(input('Comprimento (em metros): '))
larg = float(input('Largura (em metros): '))
area(comp, larg)