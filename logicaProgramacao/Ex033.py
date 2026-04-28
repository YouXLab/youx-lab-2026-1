Primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
menor = Primeiro
if segundo < Primeiro:
    menor = segundo
if terceiro < Primeiro:
    menor = terceiro
print(f'O menor valor digitado foi {menor}')
maior = Primeiro
if segundo > Primeiro:
    maior = segundo
if terceiro > maior:
    maior = terceiro
print(f'O maior valor digitado foi {maior}')