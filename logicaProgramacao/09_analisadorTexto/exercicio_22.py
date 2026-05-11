from faulthandler import is_enabled

nome= input('o nome da pessoa')
maiusculo = nome.upper()
print(f'seu nome em maiusculo é  {maiusculo}')

minusculo= nome.lower()
print(f'seu nome em minusculo é {minusculo}')

letras= len(nome)
print(f'seu {nome} tem {letras} letras ')

espaco = nome.split()
primeiro=len(espaco)
print(f'seu primeiro nome é {espaco[0]} e ele tem {len(espaco[0])} letras')