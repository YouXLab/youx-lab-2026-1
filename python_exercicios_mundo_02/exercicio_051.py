#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.


primeiro = int(input("primeiro número: "))
razao = int(input("Digite a razão: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao,razao):
    print(f"{c}", end = " " )
print("FIM")
