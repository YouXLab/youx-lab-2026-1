soma = 0
contagem = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
       soma = soma + c
       contagem = contagem + 1
print(f"A soma de todos os {contagem} valores solicitados é {soma}")




