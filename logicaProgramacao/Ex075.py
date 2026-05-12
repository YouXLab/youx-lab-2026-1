tupla = (int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: ")), int(input("Digite o quarto número: ")))
print(tupla)
nove = tupla.count(9)
print (f"O numero nove aparece {nove} vezes ")
if 3 in tupla:
    print(f"O numero 3 esta na posicao {tupla.index(3)}")
else:
    print('O Valor 3 nao esta no programa!')
print(f'Os numeros pares digitados foram ' ,end= '')
for n in tupla:
    if n % 2 == 0:
        print(n,end= '')
