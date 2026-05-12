numero = int(input('Digite um numero: '))
anterior = 0
atual = 0
contador = 0
while contador < numero:
    if contador == 0:
        print(atual)
        contador += 1
    elif contador == 1:
        atual = 1
        print(atual)
        contador += 1
    else:
        resultado = atual + anterior
        print(resultado)
        anterior = atual
        atual = resultado
        contador +=1