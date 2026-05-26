numero = int(input('Digite um número entre 0 e 20: '))
while numero > 20 or numero < 0:
    print('Número fora de 0 a 20... Tente novamente!')
    numero = int(input('Digite um número entre 0 e 20: '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número {extenso[numero]}.')
#primeiro: criei uma variavel no caso,'numero' e atribui ela a um input, ou seja, uma pergunta para obter um resultado digitado
#segundo: while(enquanto) 'numero' digitado for maior que 20 or(ou) numero for menor que 0...
#terceiro: enquanto a função acima ocorre,o programa diz que o numero esta fora de 0 a 20,pois a ideia do programa é pegar um valor entre 0 e 20...ou seja,-1 em diante ou 21 em diante não são permitidos
#quarto: portanto o programa vai perguntar de nv (até o numero digitado for um numero entre 0 e 20)
#quinto:fora do enquanto usei uma variavel com tupla e atribui os numeros de 0 a 20 escritos por extenso pois lembrando que eu quero um valor entre 0 e 20...
#sexto: printei(resposta) formatado e dentro do 'tanãnã ou chaves ({})' quero que a máquina mostre a escrita por extenso em acordo com o numero digitado...ou seja brinquei com o salvamento e a regra padrão...começa no 0 e portanto atribui a 0 a str(string/palavra) "zero"...e a mesma coisa com o 1...na range 1 atribui a str "um"



