#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista_numero = []
resposta = ''
while 'N' not in resposta:
    valor = int(input("Digite um numero para ser adicionado á lista: "))
    if valor not in lista_numero:
        lista_numero.append(valor)
        print("O valor sera adicionado")
    else:
        print("Valor nao sera adicionado")
    resposta = input("Quer continuar?[S/N] ").upper()
print(lista_numero)