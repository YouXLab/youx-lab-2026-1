from datetime import date;
h = date.today().year;
me = 0;
ma = 0;
for i in range(0, 2):
    a = int(input("Qual a idade da {}° pessoa?: ".format(i+1)))
    if (h - a) < 18:
        me += 1;
    elif (h - a) >= 18:
        ma += 1;
print("Ao todos foram preenchidos 7 pessoas, dessas {} são menores de idade e {} são maiores de idade".format(me, ma))