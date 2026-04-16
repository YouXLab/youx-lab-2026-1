r = 0;
co = 0;
for c in range(1, 501, 2):
    if c % 3 == 0:
        r += c
        co += 1
print("A soma de todos {} valores solicitados foi: {} ".format(co, r))
