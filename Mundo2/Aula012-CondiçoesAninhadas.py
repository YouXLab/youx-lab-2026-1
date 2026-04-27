#Ex:
#se carro.esqeurda()
#senao se carro.direita()
#senao

#if carro.esquerda():
#BLOCO1
#elif carro.direita():
#BLOCO2
#elif carro.ré():
#BLOCO3
#else:
#BLOCO4

#Fase pratica:
nome = str(input('Qual é seu nome? '))
if nome == 'Ana':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))