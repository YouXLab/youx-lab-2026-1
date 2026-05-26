while True:
    print("-"*40)
    print("  Menu interativo de ajuda em python")
    print("-"*40)
    comando = input("Digite o comando para obter ajuda: ").strip()
    if comando:
        help(comando)
        break