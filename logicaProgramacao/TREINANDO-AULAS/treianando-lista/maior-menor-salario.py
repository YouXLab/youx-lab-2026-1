# FUNCIONÁRIOS COM MAIOR E MENOR SALÁRIO

funcionarios = []

maior = 0
menor = 0

for i in range(3):
    pessoa = {}

    print(f"\nFUNCIONÁRIO {i+1}")

    pessoa["nome"] = input("Nome: ")
    pessoa["salario"] = float(input("Salário: R$ "))

    funcionarios.append(pessoa)

    if i == 0:
        maior = pessoa["salario"]
        menor = pessoa["salario"]
    else:
        if pessoa["salario"] > maior:
            maior = pessoa["salario"]

        if pessoa["salario"] < menor:
            menor = pessoa["salario"]

print("\nRELATÓRIO")
print("-" * 35)

for f in funcionarios:
    print(f"Nome: {f['nome']}")
    print(f"Salário: R$ {f['salario']:.2f}")
    print("-" * 35)

print(f"Maior salário: R$ {maior:.2f}")
print(f"Menor salário: R$ {menor:.2f}")