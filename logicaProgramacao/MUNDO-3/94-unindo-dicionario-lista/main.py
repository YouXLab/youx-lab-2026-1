dicionario = {}
lista= []
contagem = 0
media = 0
while True:
    contagem += 1
    dicionario["nome"] = input("Nome: ").strip()
    sx = input("Sexo [M/F]: ").strip()[0]
    while True:
        if sx in "MmFf":
            dicionario["sexo"] = sx
            break
        else:
            print("Sexo invalido! Use apenas M ou F")
            sx = input("Sexo [M/F]: ").strip()[0]
    dicionario["idade"] = int(input("Idade: "))
    media += dicionario["idade"]
    o = input("Quer continuar? [S/N]: ").strip()[0]
    while o not in "SsNn":
            print("Opção invalida use apenas S ou N")
            o = input("Quer continuar? [S/N]: ").strip()[0]
    lista.append(dicionario.copy())
    if o in "Nn":
        break
    dicionario.clear()
    print("-"*20)
print("-="*25)
print(f"A) Ao todo temos {len(lista)} pessoas cadastradas.")
print(f"B) A média de idade é de {media / len(lista)} anos.")
com = []
for i, e in enumerate(lista):
    if e["sexo"] in "Ff":
        com.append(e["nome"])
if com:
    print("C) As mulheres registradas foram: ", end="")
    for i, e in enumerate(com):
        if i+1 == len(com):
            print(e)
        else:
            print(f"{e}, ", end="")
else:
    print("C) Não tivemos mulheres cadastradas")
print(f"D) Lista das pessoas com idade acima da média:")
for i in lista:
    for n, v in enumerate(i):
        if i['idade'] > (media / len(lista)):
            print(f" {v} = {i[v]}; ", end="")
    print()
print("<< ENCERRADO >>")