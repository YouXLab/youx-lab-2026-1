from random import randint
numeros = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))
print("Os números sorteados foram:", end="")
for numerais in numeros:
    print(f'{numerais}', end="")
print(f"\nO maior número foi: {max(numeros)}")
print(f"O menor número foi: {min(numeros)}")

#Para começar eu importei da biblioteca 'random'(aleatorio) a função randint(sorteio aleatorio)
#então criei uma variavel com tupla 5x de numeros aleatorios que a máquina vai gerar para mim...
#agora é a parte complicada/meio confusa...fiz um print(resposta) e usei o end="" para fazer o print NÃO quebrar a linha...
#continuando: for(para) numerais(variavel aleatoria só para o "for" funcionar) in(em) numeros:
#printei(resposta) as 'respostas' dos numeros gerados pela máquina e novamente usei o end="" para NÃO quebrar a linha
#no fim eu quebrei a linha(sim deve se consertar essa parte porque tem informações inuteis/irrelevantes) e printei o valor maximo de 'numero'
#printei o menor valor de 'numero'


