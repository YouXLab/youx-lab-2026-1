nome = input("Nome:  ")
gols = input("Gols:  ")

if not nome:
    nome= "Desconhecido"
if not gols or not gols.isnumeric():
    gols=0

print(f"Nome: {nome} e Gols: {gols}")




