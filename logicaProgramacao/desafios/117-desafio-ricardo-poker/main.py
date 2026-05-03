import defs
mao = [("A", "♠"), ("K", "♦")]

mesa = [
    ("Q", "♠"),
    ("J", "♠"),
    ("10", "♠"),
    ("2", "♦"),
    ("3", "♣")
]

print(defs.avaliar_mao(mao + mesa))