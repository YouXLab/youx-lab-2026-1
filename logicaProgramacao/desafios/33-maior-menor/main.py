n1 = int(input("Digite o valor 1: "));
n2 = int(input("Digite o valor 2: "));
n3 = int(input("Digite o valor 3: "));
ma = n1;
me = n1;
if n2 > ma:
    ma = n2;
else:
    if n2 < me:
        me = n2;
        
if n3 > ma:
    ma = n3;
else: 
    if n3 < me:
        me = n3;
if n1 > ma:
    ma = n1;
else: 
    if n1 < me:
        me = n1;
print("O maior número digitado foi {} e o menor foi {}".format(ma, me))