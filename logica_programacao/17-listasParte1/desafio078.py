#Exercício Python 078: Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas posições na lista.

lista_de_numeros = []
maior = 0
menor = 0
for contagem in range(0, 5):
    print('==='*25)
    lista_de_numeros.append(int(input(f"Me diga qual valor ficará na posição {contagem+1}: ")))
    print('===' * 25)
    if contagem == 0:
        maior = menor = lista_de_numeros[contagem]
    else:
        if lista_de_numeros[contagem] > maior:
            maior = lista_de_numeros[contagem]
        else:
            if lista_de_numeros[contagem] < menor:
                menor = lista_de_numeros[contagem]
print('==='*25)
print(f'Você digitou os valores:{lista_de_numeros}')
print(f'O maior valor digitado foi: {maior}')
print(f"O menor valor foi: {menor}")
print('==='*25)
print('')
print("Programa Finalizaaaaaaaaaaaado.")

#Bora para a explicação:para começar eu criei uma variavel para uma lista, chamada "lista_de_numeros"
#Para medir o maior e o menor eu criei 2 variaveis e atribui o valor delas a 0
#for(para) contagem in(em) range de 0,5 porque eu fiz isso? para fazer 4 perguntas...atraves do input criado abaixo...
#if(se) a contagem for igual a 0 maior recebe menor que recebe lista_de_numeros[contagem] <---(Motivo:em lista_de_numeros peguei contagem)






