lista = list()
def maior(*num):
    print(f'Maior numero da lista dos numeros citados: {max(lista)}')
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    else:
        lista.append(num)
maior(max(lista))

