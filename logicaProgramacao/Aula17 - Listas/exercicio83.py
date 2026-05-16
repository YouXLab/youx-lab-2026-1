#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite sua espressao: '))

aberto = expressao.count('(')
fechado = expressao.count(')')

if aberto != fechado:
    print('Expressão INVÁLIDA...')
else:
    print('Expressão VÁLIDA...')