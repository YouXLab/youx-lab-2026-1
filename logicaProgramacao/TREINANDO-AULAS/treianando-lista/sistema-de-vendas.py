# SISTEMA DE VENDAS
# Lista + Dicionário + FOR + comissão

vendedores = []

for i in range(3):
    vendedor = {}

    print(f"\nVENDEDOR {i+1}")

    vendedor["nome"] = input("Nome: ")

    vendedor["vendas"] = float(input("Valor vendido: R$ "))

    vendedor["comissao"] = vendedor["vendas"] * 0.05

    vendedor["total"] = vendedor["vendas"] + vendedor["comissao"]

    vendedores.append(vendedor)

print("\nRELATÓRIO")
print("-" * 40)

for v in vendedores:
    print(f"Vendedor: {v['nome']}")
    print(f"Vendas: R$ {v['vendas']:.2f}")
    print(f"Comissão: R$ {v['comissao']:.2f}")
    print(f"Total a receber: R$ {v['total']:.2f}")
    print("-" * 40)