lista = []
continuacao = 'S'
procurado = 5
while continuacao == 'S':
    print('-=-' * 10)
    valor = int(input("Digite um número: "))
    print('Valor adicionado com sucesso...')
    continuacao = str(input('Deseja Continuar? [S/N]: ')).upper().strip()

    if not(valor in lista):
        lista.append(valor)

    if continuacao == 'N':
        print('-=-' * 10)
        print(f"Foram digitados {len(lista)} numeros")
        print('-=-' * 10)
        lista.sort(reverse=True)
        print(f"Em ordem decrescente: {lista}")
        print('-=-' * 10)
        if procurado in lista:
                print(f"O Numero 5 esta na lista")

        else:
            print('O Numero 5 nao esta na lista')
            print('-=-' * 10)

