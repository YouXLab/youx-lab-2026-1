#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será
# mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(numero, show=False):
    """
    Calcula o Fatorial de um número
    :param num:  -- > Número desejado (int)
    :param show: -- > Se deseja que o processo de cálculo seja apresentado (lógico -boolean)
    :return:
    """
    dec = numero
    count = 0
    resultado = 0
    fatorial = ''
    while count < numero:
        count += 1
        fatorial += str(dec) + 'x'
        if count > 1:
            resultado = (resultado * dec)
        else:
            resultado = numero
        dec -= 1
    if show:
        print(fatorial[:len(fatorial)-1], '=', '{}'.format(resultado))
    else:
        print(resultado)
fatorial(5, True)
help(fatorial)
