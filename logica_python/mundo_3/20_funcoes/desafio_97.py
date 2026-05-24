
def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)
escreva('Oi')
escreva('Tudo bem.')
escreva('Tenha um otimo dia. ')