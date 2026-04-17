ma = 0;
me = 0;
for i in range(0, 7):
    p = float(input("Digite o peso da {}° pessoa: ".format(i+1)));
    if i+1 == 1:
        ma = p;
        me = p;
    else:
        if p > ma:
            ma = p
        elif p < me:
            me = p;
print("O maior peso inserido foi {} e o menor foi {}".format(ma, me))