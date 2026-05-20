from time import sleep

class Livro:
    def __init__(self, livro, paginas):
        self.nome = livro
        self.paginas = paginas
        self.contador = 0
        print(f'você acabou de abrir o livro "{self.nome}" que tem {self.paginas} páginas. Você está na pagina 1')
    def avancar_paginas(self, pagina):
        if self.contador == 0:
            for p in range(2, pagina+2):
                print(f'Pág{p} >', end=' ')
                self.contador += 1
                sleep(0.3)
            print(f'Você avançou {pagina} e agora está na pagina {p}')
        elif pagina > self.paginas:
            paginas = 0
            for p in range(self.contador+2, self.paginas+1):
                print(f'Pág{p} >', end=' ')
                paginas +=1
                sleep(0.3)
            print(f'Você avançou {paginas} e agora está na pagina {p}')
            print(f'Você chegou ao fim do livro "{self.nome}"')
        elif self.contador > 0:
            for p in range(self.contador + 2, self.contador + 2 + pagina):
                print(f'Pág{p} >', end=' ')
                self.contador += 1
                sleep(0.3)
            print(f'Você avançou {pagina} e agora está na pagina {p}')
livro = Livro('10 coisas que aprendi', 20)
livro.avancar_paginas(5)
livro.avancar_paginas(10)
livro.avancar_paginas(100)