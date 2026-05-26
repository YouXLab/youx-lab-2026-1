def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'A aŕea de um terreno {largura}x{comprimento} é de {resultado}m².')

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)