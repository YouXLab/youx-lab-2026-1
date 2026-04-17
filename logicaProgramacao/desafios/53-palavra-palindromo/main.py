f = input("Digite a frase ou palavra:");
fl = f[::-1].lower().replace(" ", "");
if fl == f.replace(" ", ""):
    print("A frase {} ao contrário fica: {} ou seja, ela é palindromo".format(f, f));
else:
    print("A frase {} ao contrário fica: {} ou seja, ela não é palindromo".format(f, f[::-1]));