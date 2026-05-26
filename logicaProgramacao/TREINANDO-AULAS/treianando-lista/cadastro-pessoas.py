# CADASTRO DE PESSOAS
# Lista + Dicionário + FOR + análise

pessoas = []
maiores = 0
menores = 0

for i in range(4):
    pessoa = {}

    print(f"\nPESSOA {i+1}")

    pessoa["nome"] = input("Nome: ")
    pessoa["idade"] = int(input("Idade: "))

    if pessoa["idade"] >= 18:
        pessoa["situacao"] = "Maior de idade"
        maiores += 1
    else:
        pessoa["situacao"] = "Menor de idade"
        menores += 1

    pessoas.append(pessoa)

print("\nRELATÓRIO")
print("-" * 35)

for p in pessoas:
    print(f"Nome: {p['nome']}")
    print(f"Idade: {p['idade']}")
    print(f"Situação: {p['situacao']}")
    print("-" * 35)

print(f"Maiores de idade: {maiores}")
print(f"Menores de idade: {menores}")