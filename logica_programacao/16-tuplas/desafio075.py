valores = tuple(int(input('Digite alguns valores:'))for conte in range(1, 5))
print(f'O número 9 apareceu: {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na: {valores.index(3)+1}º posição'
    if 3 in valores
    else 'Valor 3 não foi digitado')
print('Valores pares digitados foram:', end=' ')
print({numero for numero in valores if numero % 2 == 0}, end=' ')
print('')
print("\nPrograma Finalizado!\nObrigado ;)")
print('')

#começando eu descobri pelos comentários que é possivel fazer uma tupla usando "tuple",ent fiz uma tupla do input e for(para) contar na range de 1,5...o que isso significa? vai salvar em uma tupla dos valores que forem digitados e usei o for para fazer a máquina fazer e armazenar as respostas das perguntas 4x pois 1 , 5 começa do 1 e terina no 5 desconsiderando o 5 ou seja 4x
#printei um dos objetivos,usei o ".count" para o programa contar quantas x o 9 apareceu nas respostas coletadas anteriormente
#outro print dessa vez para saber em qual posição o 3 foi encontrado(se n tiver fiz depois) usei o ".index()" para isso e dentro do () coloquei o 3 que é o número escolhido para essa informação...coloquei +1 para não começar da posição 0° e sim começar da 1°
#ai if 3 in(em) valores estiver...
#elif (senão se) mostrar que o 3 não foi digitado
#printei o próximo passo que será mostrar os valores pares...
#print usei o {} para criar um dicionário numero para numero em valores se o resto da divisão de número for 0 ou seja par...end=" " (para n quebrar linha usei o end=" ")
#por fim está de boa...





