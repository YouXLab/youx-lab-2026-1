from gettext import find

nome = str(input('Digite seu nome completo: ')).strip()
print('Vocẽ tem silva no nome? {} '.format('SILVA ' in nome.upper()))