print('         VALORES')
print('-=-' * 10)
lista = []
continuacao = 'S'
while continuacao == 'S':
    valor = int(input("Digite um número: "))
    print('Valor adicionado com sucesso...')
    continuacao = str(input('Deseja Continuar? [S/N]: ')).upper().strip()


    if not(valor in lista):
        lista.append(valor)


    if continuacao == 'N':
        print('-=-' * 10)
        print(f"Voce digitou os valores {lista}")
        print('-=-' * 10)
        print(f"O Maior Numero foi: {max(lista)}")
        print('-=-' * 10)
        print(f"O Menor Numero foi: {min(lista)}")
        print('-=-' * 10)
        for indice,item in enumerate(lista):
            print(f'Em suas respectivas posicoes os numeros sao {item} e {indice}º')

    elif continuacao != 'S':
        print('Resposta Invalida!')