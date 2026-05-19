#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.


primeiro = int(input("primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 1
while contador <= 10:
    if contador == 1:
        print(primeiro, end=" -> ")
    segundo = primeiro + razao
    print(segundo, end=' -> ')
    primeiro = segundo
    contador += 1
print("fim")
