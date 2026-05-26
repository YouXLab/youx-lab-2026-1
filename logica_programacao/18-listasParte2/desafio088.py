from random import sample
print("JOGO DA MEGA SENA...")
quantidade = int(input('Quantas apostas gerar? '))
numero = [sample(range(1, 61), k=6) for jogadas in range(0, quantidade)]
for contagem in range(0, quantidade):
    print(f'Aposta {contagem + 1}: {sorted(numero)[contagem]}')


