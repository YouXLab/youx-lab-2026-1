#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será
# mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    Calcula o Fatorial de um número
    :param num:  -- > Número desejado (int)
    :param show: -- > Se deseja que o processo de cálculo seja apresentado (lógico -boolean)
    :return:
    """
    dec = num
    count = 0
    result = 0
    fat = ''
    while count < num:
        count += 1
        fat += str(dec) + 'x'
        if count > 1:
            result = (result * dec)
        else:
            result = num
        dec -= 1
    if show:
        print(fat[:len(fat)-1], '=', '{}'.format(result))
    else:
        print(result)
fatorial(5, True)
help(fatorial)