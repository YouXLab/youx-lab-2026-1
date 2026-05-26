#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior
# e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('======'*15)
print('BRINCANDO COM SOMA,MENOR,MAIOR,MÉDIA NA MATEMÁTICA.........')
print('======'*15)
resposta = 'S' # resposta vai receber a str "S" para sim
soma = quantidade = media = maior = menor =  0 # criei essas variaveis e atribui '0' a elas
while resposta in "Ss": #se a resposta for sim...
    numero = int(input('ME DIGA UM NÚMERO:')) # pergunta criada
    soma = soma + numero # "guardando" as somas para a dinâmica da atividade
    quantidade = quantidade + 1 # "guardando" as quantidades para o final da atividade na parte de média!
    if resposta == 1: # a partir do "1" se a resposta for igual à um...
        maior = menor = numero #maior vai receber menor que vai receber numero,vão ser iguais eu acho
    else: # se não...
        if numero > maior: #se 'número' for maior que 'maior' logo:
            maior = numero #será atribuido à 'maior','numero'
        elif numero < menor: #senão, se numero for menor que 'menor' fiz o oposto do 'maior'
            menor = numero # será atribuido à 'menor','numero'
    resposta = str(input('QUER CONTINUAR?[S/N]:')).upper().strip()[0] #upper para deixar tudo em maiusculo e strip para remover espaços e outras demais informações irelevantes...e o '[0]' é porque vai começar no 0° termo e só ele vai valer...
media = soma / quantidade # media é a soma de tudo dividido pela quantidade de algaritmos: ex: 3+3+3 para saber a média faço a soma de tudo que resulta em 9 e divido pela quantidade de termos nesse caso 3...logo a média é 9 / 3 = 3
print(f'A SOMA DOS NÚMEROS QUE VOCÊ DIGITOU RESULTAM EM: {soma}\nE A MÉDIA DELES É: {media}') #'resposta 1/primeira parte'
print(f'O MAIOR NÚMERO FOI: {maior} E O MENOR NÚMERO FOI: {menor}')#'resposta 2/segunda parte'





