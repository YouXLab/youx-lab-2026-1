dados = []
dadosPessoais = {}
continuar = 'S'
while continuar != "N":
    dadosPessoais["nome"] = str(input("Digite o seu nome: "))
    dadosPessoais["sexo"] = str(input("Qual o seu sexo? [M/F] ")).upper()
    dadosPessoais["idade"] = int(input("Qual a sua idade: "))
    dados.append(dadosPessoais.copy())
    continuar = str(input("Quer continuar? [S/N]")).upper()

print(f"Foram cadastradas {len(dados)} pessoas.")

somaIdade = 0
for dado in dados:
    somaIdade += dado["idade"]
media = somaIdade / len(dados)
print(f"A média das idades é: {media}")

mulheres = []
for dadoM in dados:
    if dadoM["sexo"] == "F":
        mulheres.append(dadoM["nome"])
print("As mulheres cadastradas foram: ", end='')
for nome in mulheres:
    print(nome, end=' ')
print()

print("Lista das pessoas que tem idade acima da média: ")
for c in dados:
    if c["idade"] > media:
        print(f"Nome: {c["nome"]}; sexo: {c["sexo"]}; idade: {c["idade"]}")
