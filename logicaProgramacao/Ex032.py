from datetime import date
Ano = int(input('Digite que voce quer analisar: '))
if Ano == 0:
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 == 0 and Ano % 400 == 0:
    print(f'O Ano {Ano} e bissexto')
else:
    print(f'O Ano {Ano} nao e bissexto')
