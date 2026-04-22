primeiro = int(input('Primeiro termo: '));
r = int(input('Razão: '));
decimo = primeiro + (10 - 1) * r
for c in range(primeiro, decimo + r, r):
    print('{}'.format(c), end=' → ');
print('ACABOU');