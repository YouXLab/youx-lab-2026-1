# CADASTRO usando lista e dicionário
dados = []

for i in range(3):
    pessoa = {}

    pessoa["nome"] = input("Nome: ")
    pessoa["idade"] = int(input("Idade: "))

    dados.append(pessoa)

print("-" * 20)

for p in dados:
    print(f"{p['nome']} tem {p['idade']} anos")