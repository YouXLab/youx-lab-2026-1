"""Exercício Python 079: Crie um programa onde o usuário possa
digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, el e não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. """
resposta = None
valores = list ()
while resposta != 'N':
    valor_atual = int(input('Digite um valor: '))
    valores.append(valor_atual)
    if valores.count(valor_atual) >1:
        valores.remove(valor_atual)
        print('Não foi possível adicionar esse número.')
    else:
        print('Número adicionado com sucesso.')
    resp=str(input('Quer continuar? [S/N]: '))
    resposta = resp.upper()
    if resposta != 'S':
        break
print('≃'*30)
print(sorted(valores))
