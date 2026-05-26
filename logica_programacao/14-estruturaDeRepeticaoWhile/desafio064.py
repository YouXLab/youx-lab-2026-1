print('====='*7)
print('JOGO DAS SOMAS QUASE INFINITAS')
print('====='*7)
numero_para_somar = quantidade = somatorio = 0
numero = int(input('DIGITE UM NÚMERO PARA SOMAR [USE 999 PARA PARAR]:'))
while numero != 999:
    somatorio = somatorio + numero
    quantidade = quantidade + 1
    numero = int(input('DIGITE UM NÚMERO PARA SOMAR [USE 999 PARA PARAR]:'))

print(f'VOCÊ SOMOU {quantidade} ALGARITMOS...O RESULTADO DA SOMA DESSES ALGARITMOS FOI {somatorio}')













