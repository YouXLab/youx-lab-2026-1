from time import sleep

def contador(i, f, p):
    print('-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p == 0:
        p = 1

    # Crescente
    if i < f:
        while i <= f:
            print(i, end=' ')
            sleep(0.5)
            i += p

    # Regressiva
    else:
        while i >= f:
            print(i, end=' ')
            sleep(0.5)
            i -= p

    print('FIM!')
    print('-' * 20)


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Contagem personalizada')


#Importa a função sleep(), que faz o programa “esperar” alguns segundos.

#3 parâmetros:
#* i → início
#* f → fim
#* p → passo

#Se a pessoa digitar passo 0, o programa troca para 1.
#Porque não existe contagem pulando de 0 em 0.

#Enquanto i for menor ou igual ao fim, ele continua repetindo.

