def aumentar(preco, taxa):
    return preco + (preco * taxa / 100)


def diminuir(preco, taxa):
    return preco - (preco * taxa / 100)


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2


# --- Teste do código ---
if __name__ == "__main__":
    p = 100.0
    print(f"Preço base: R$ {p:.2f}")
    print(f"Aumentando 10%: R$ {aumentar(p, 10):.2f}")
    print(f"Diminuindo 10%: R$ {diminuir(p, 10):.2f}")
    print(f"O dobro é: R$ {dobro(p):.2f}")
    print(f"A metade é: R$ {metade(p):.2f}")




