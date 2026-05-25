#def soma(a, b):...

#Programa principal
#soma(4,5)
#soma(8,9)
#soma(2,1)
#soma(4, 1)
#def contador(* num):
 #   print(num)
#contador(2,1,7)
#contador(8,0)
#contador(4,4,7,6,2)


def soma(* valores):
    s =0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')
soma(5,2)
soma(2,9,4)
