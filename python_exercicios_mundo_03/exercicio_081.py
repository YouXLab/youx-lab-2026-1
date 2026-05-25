#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


valor = []
resposta = "S/N"
while resposta not in "N":
    valor.append(int(input("Digite um valor: ")))
    resposta = str(input("Quer continuar? [S/N] "))
    print(f"Foram digitados {len(valor)} números")
    valor.sort(reverse = True)
    print(f"Em ordem decrescente {valor}")
    if 5 in valor:
        print("O valor 5 faz parte da lista")
    else:
        print("O valor 5 não foi encontrado")
