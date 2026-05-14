n = int(input("Quantos termos você quer mostrar? "))

t1 = 0
t2 = 1
cont = 3

if n <= 0:
    print("Por favor, digite um número maior que zero.")
elif n == 1:
    print(f"{t1}")
else:
    print(f"{t1} - {t2}", end="")
    while cont <= n:
        t3 = t1 + t2
        print(f" - {t3}", end="")
        t1 = t2
        t2 = t3
        cont += 1
    print()
