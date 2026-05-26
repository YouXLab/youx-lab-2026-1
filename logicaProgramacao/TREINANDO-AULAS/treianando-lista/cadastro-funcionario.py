# CADASTRO DE FUNCIONÁRIOS
# Lista + Dicionário + FOR + cálculo de aumento

funcionarios = []

for i in range(3):
    dados = {}

    print(f"\nFUNCIONÁRIO {i+1}")

    dados["nome"] = input("Nome: ")

    dados["salario"] = float(input("Salário: R$ "))

    if dados["salario"] <= 2000:
        aumento = dados["salario"] * 0.15
    else:
        aumento = dados["salario"] * 0.10

    dados["aumento"] = aumento
    dados["novo_salario"] = dados["salario"] + aumento

    funcionarios.append(dados)

print("\n" + "-" * 40)
print("RELATÓRIO DOS FUNCIONÁRIOS")
print("-" * 40)

for f in funcionarios:
    print(f"Nome: {f['nome']}")
    print(f"Salário atual: R$ {f['salario']:.2f}")
    print(f"Aumento: R$ {f['aumento']:.2f}")
    print(f"Novo salário: R$ {f['novo_salario']:.2f}")
    print("-" * 40)