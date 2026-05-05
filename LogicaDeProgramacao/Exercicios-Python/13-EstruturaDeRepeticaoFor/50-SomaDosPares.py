N1 = 0
N2 = 0
for c in range(1,7):
    N3 = int(input(f'Digite o {c} valor:'))
    if N3 % 2 == 0:
        N1 += N3
        N2 += 1
print(f'Você colocou {N2} numeros pares e a soma foi {N1}.')