def si(ano):
    from datetime import date
    hoje = date.today().year
    atual = hoje - ano
    if atual < 15:
        print(f"Com {atual} anos o voto é proibido")
    if atual >= 16 and atual < 18 or atual >= 65:
        print(f"Com {atual} anos o voto é opcional")
    if atual >= 18 and atual < 65:
        print(f"Com {atual} anos o voto é obrigatório")
si(int(input("Seu ano de nascimento: ")))