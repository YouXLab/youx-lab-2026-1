nome =str(input('Qual é o seu nome?:'))
mai =nome.upper()
min =nome.lower()
contaLetra = len(nome) - nome.count(' ')
print('Seu nome em maiúsculo é:', mai)
print('Seu nome em minúsculo é:', min)
print(f'Seu nome ao todo tem {contaLetra} letras')
primeiroNome = (nome.find(' '))
print(f'Seu 1° nome tem: {primeiroNome} letras')


