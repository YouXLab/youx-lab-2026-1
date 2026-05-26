#Exercício Python 083: Crie um programa onde o usuário digite uma expressão
# qualquer que use parênteses. O aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite a expressão: '))
conte = 0
for contagem in expressao:
    if contagem == '(':
        conte += 1
    elif contagem == ')':
        conte -= 1
        if conte < 0:
            break

if conte == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida')
























