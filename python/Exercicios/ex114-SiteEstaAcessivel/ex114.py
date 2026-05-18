import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br')
except urllib.error.URLError:
    print('O site "Pudim" não está acessivel no momento!')
else:
    print('Consegui acessar o site "Pudim" com sucesso!')