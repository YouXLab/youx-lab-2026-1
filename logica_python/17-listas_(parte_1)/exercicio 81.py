valores = []

while True:
    n = int(input("Digite um valor: "))
    valores.append(n)

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == 'N':
        break
print(f"\nA) Foram digitados {len(valores)} números.")
valores.sort(reverse=True)
print(f"B) Os valores em ordem decrescente são: {valores}")
if 5 in valores:
    print("C) O valor 5 foi digitado e está na lista.")
else:
    print("C) O valor 5 NÃO foi digitado.")

