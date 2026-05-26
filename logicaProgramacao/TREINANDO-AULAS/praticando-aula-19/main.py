produto = {
    "nome": "Notebook",
    "preco": 4500.00,
    "disponivel": True,
    "estoque": 15
}

# Acessando valores usando a chave
print(produto["nome"])    # Saída: Notebook
print(produto["preco"])   # Saída: 4500.0

# Adicionando um novo item
produto["cor"] = "Prata"

# Atualizando um valor existente
produto["estoque"] = 20

print(produto)

