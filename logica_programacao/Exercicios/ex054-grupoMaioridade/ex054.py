from datetime import date
idadeatual= date.today().year
for c in range(1,8):
 nascimento= int(input('em que ano a pessoa nasceu?'))
 idade = idadeatual - nascimento
 if idade >= 18:
     print('a pessoa é maior de idade')
 else:
     print('a pessoa é menor de idade')