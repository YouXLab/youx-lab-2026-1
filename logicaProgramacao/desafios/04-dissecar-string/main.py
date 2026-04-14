texto = input("Digite algo: ");

print("O tipo do texto acima é: ", type(texto));
print("Só tem espaço?: ", texto.isspace());
print("É numerico?: ", texto.isnumeric());
print("É alfabético?: ", texto.isalpha());
print("É alfanumerico?: ", texto.isalnum());
print("São todas maiusculas: ", texto.isupper());
print("São todas minusculas?: ", texto.islower());
print("O texto está capitalizado?: ", texto.istitle)