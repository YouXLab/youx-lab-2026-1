from datetime import date
ano = int(input('me diga um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é bissexto')
else:
 print('o ano não é bissexto')