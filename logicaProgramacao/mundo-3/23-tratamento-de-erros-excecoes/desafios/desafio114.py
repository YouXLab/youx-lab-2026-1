import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
    print('O site Pudim não está acessivel no momento.')
except:
    print('Consegui acessar o site Pudim com sucesso.')