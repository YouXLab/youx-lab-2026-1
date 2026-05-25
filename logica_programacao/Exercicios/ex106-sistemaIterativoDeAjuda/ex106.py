def ajuda():
    comando= input('funcao ou biblioteca: ').upper()
    while comando != 'fim':
        help(comando)
        comando=input('funcao ou biblioteca: ').upper()
    print('programa encerrado!')
ajuda()


