lista = (
    "lapis", 1.75,
    "Borracha", 2,
    "Caderno", 15.90,
    "Estojo", 25,
    "Transferidor", 4.20,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Canetas", 22.30,
    "Livro", 34.90)

print('LISTAGEM DE PREÇOS')
for contagem, precos in enumerate(lista):
    if contagem % 2 == 0:
        print(f"{lista[contagem]:.<15}", end="")
    else:
        print(f"R$ {lista[contagem]:>1.2f}")
