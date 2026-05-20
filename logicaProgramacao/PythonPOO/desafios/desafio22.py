from rich import print


class ControleRemoto:
    def __init__(self):
        self.ligada = False
        self.volume = 0
        self.canal_atual = 1
        self.canal_maximo = 5
        self.canal_minimo = 1
        self.volume_maximo = 5
        self.volume_minimo = 0
        self.comando = ''

    def controle(self):
        self.comando = str(input('A TV está desligada - Use @ para ligá-la: (0 encerrar programa) '))
        while self.comando not in '@><-+0':
            print('Comando inválido. Tente novamente')
            self.comando = str(input('A TV está desligada - Use @ para ligá-la: (0 encerrar programa) '))

    def ligar(self):
        if self.comando == '@':
            self.ligada = True

    def desligar(self):
        self.ligada = False
        self.comando = str(input('A TV está desligada - Use @ para ligá-la: (0 encerrar programa) '))

    def prox_canal(self):
        if self.canal_atual == self.canal_maximo:
            self.canal_atual = self.canal_minimo
        else:
            self.canal_atual += 1

    def voltar_canal(self):
        if self.canal_atual == self.canal_minimo:
            self.canal_atual = self.canal_maximo
        else:
            self.canal_atual -= 1

    def aumentar_volume(self):
        if self.volume == self.volume_maximo:
            self.volume = self.volume_maximo
        else:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume == self.volume_minimo:
            self.volume = self.volume_minimo
        else:
            self.volume -= 1

    def status(self):
        print('TV ligada')
        self.comando = str(input(f'< CH{self.canal_atual} >   - VOL{self.volume} + '))

c1 = ControleRemoto()
c1.controle()
while c1.comando != '0':
    c1.status()
    match c1.comando:
        case '>':
            c1.prox_canal()
        case '<':
            c1.voltar_canal()
        case '+':
            c1.aumentar_volume()
        case '-':
            c1.diminuir_volume()
        case '@':
            c1.desligar()