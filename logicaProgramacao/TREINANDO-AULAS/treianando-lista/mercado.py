# MERCADO
# Lista + Dicionário + FOR + soma total

produtos = []
total = 0

for i in range(3):
    produto = {}

    print(f"\nPRODUTO {i+1}")

    produto["nome"] = input("Nome do produto: ")

    produto["preco"] = float(input("Preço: R$ "))

    produto["quantidade"] = int(input("Quantidade: "))

    produto["subtotal"] = produto["preco"] * produto["quantidade"]

    total += produto["subtotal"]

    produtos.append(produto)

print("\nNOTA FISCAL")
print("-" * 40)

for p in produtos:
    print(f"Produto: {p['nome']}")
    print(f"Quantidade: {p['quantidade']}")
    print(f"Subtotal: R$ {p['subtotal']:.2f}")
    print("-" * 40)

print(f"TOTAL DA COMPRA: R$ {total:.2f}")