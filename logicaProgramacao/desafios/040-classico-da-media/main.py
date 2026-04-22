p = float(input('Primeira nota: '));
s = float(input('Segunda nota: '));
m = (p + s) /2;
if m >= 7:
    media = 'APROVADO';
elif m < 5:
    media = 'REPROVADO';
else:
    media = 'RECUPERAÇÃO';
print(f"Tirando {p:.2f} e {s:.2f}, a média do aluno é {m:.2f}\nO aluno está {media}.");