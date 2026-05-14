
print('______'*5)
print('SEQUÊNCIA DE FIBONACCI......')
print('______'*5)
numero_de_termos = int(input('ATÉ QUAL TERMO VOCÊ QUER VER?:'))
ultimo_termo= 1
penultimo_termo = 0
print('0 - 1 - ', end='')
for contagem in range(2, numero_de_termos):
    termo_atual = ultimo_termo + penultimo_termo
    print(f"{termo_atual} - ", end='')
    penultimo_termo = ultimo_termo
    ultimo_termo = termo_atual

print('FIM')









