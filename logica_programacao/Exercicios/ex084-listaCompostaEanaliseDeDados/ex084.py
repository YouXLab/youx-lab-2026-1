galera=list()
dados=list()
continuar = "S"
maior=0
menor=0
while continuar != "N":
    dados.append(str(input('qual seu nome? ')))
    dados.append(float(input('qual seu peso? ')))
    galera.append(dados[:])
    dados.clear()
    continuar = str(input("Quer continuar? [S/N]")).upper()
print(f'foram cadastradas {len(galera)} pessoas')
for c in range(0, len(galera)):
    if c == 0:
        menor = galera[0][1]
        maior = galera[0][1]
    else:
        if galera[c][1] > maior:
            maior = galera[c][1]
        elif galera[c][1] < menor:
            menor = galera[c][1]

print(f"O maior peso é: {maior} \n e o menor peso é {menor}")


