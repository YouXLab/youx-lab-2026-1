nome = str(input('Qual é o seu nome completo?:'))
verdadeiro = 'Silva'in nome.title().strip()
print(f'Seu nome tem Silva?: {verdadeiro}')