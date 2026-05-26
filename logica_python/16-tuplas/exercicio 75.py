num = (
    int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("Digite o quarto número: ")))

print("-" * 30)
print(f"Você digitou os valores: {num}")

print(f"A) O valor 9 apareceu {num.count(9)} vez(es).")

if 3 in num:
    print(f"B) O primeiro valor 3 foi digitado na {num.index(3) + 1}ª posição.")
else:
    print("B) O valor 3 não foi digitado em nenhuma posição.")

print("C) Os números pares digitados foram: ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
print()
