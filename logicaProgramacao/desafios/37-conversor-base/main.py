b = int(input("Digite um número inteiro: "));
print("Escolha uma das base para conversão: ");
print("1 - Converter para Binário");
print("2 - Converter para Octal");
print("3 - Converter para Hexadecimal");
o = int(input("Digite sua opção: "));
if o == 1:
    print("o número {} convertido para Binário é {}".format(b, bin(b)[2:]));
elif o == 2:
    print("O número {} convertido para Octal é {}".format(b, oct(b)[2:]));
elif o == 3:
    print("O número {} convertido para Octal é {}".format(b, hex(b)[2:]));