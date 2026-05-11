print('-=' * 10)
primeiro= int(input('digite o primeiro termo: '))
razao= int(input('razao do pa'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end='')
        termo += razao
        cont += 1
    mais = int(input("quantos termos voce quer mostrar a mais? "))
print(f"finalizando com {total} termos mostrados")