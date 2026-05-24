
def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} * {comprimento} é de {a}m².')
print(' Controle de terrenos. ')
print( '-~-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)