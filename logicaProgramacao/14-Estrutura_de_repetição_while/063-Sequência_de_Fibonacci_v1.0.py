print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)
termos_de_numero=int(input('Quantos termos você quer mostrar? '))
termo_ultimo = 1
termo_penultimo = 0
print('0 - 1 -',end='')
for contagem in range(2, termos_de_numero):
    termo_atual = termo_ultimo + termo_penultimo
    print(f'{termo_atual} - ', end='')
    termo_penultimo = termo_ultimo
    termo_ultimo = termo_atual
print('acabou')
