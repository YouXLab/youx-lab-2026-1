from rich import print
class controleRemoto:
    def __init__(self, canal = 1, volume = 2):
        self.canalAtual:int = canal
        self.canalMin: int = 1
        self.canalMax: int = 5
        self.volumeAtual:int = volume
        self.volMin: int = 1
        self.volMax: int = 5
        self.ligado:bool = False
        self.comando = ''
    def controle(self):
        self.comando = str(input('A TV está desligada - Use @ para ligá-la: (0 encerrar programa) '))
        while self.comando not in '0><-+@':
            print('Comando inválido. Tente novamente')
            self.comando = str(input('A TV está desligada - Use @ para ligá-la: (0 encerrar programa) '))
    def ligar(self):
        if self.comando == '0':
            self.ligada = True
    def desligar(self):
        self.ligada = False
        self.comando = str(input('A TV está desligada - Use 0 para ligá-la: (0 encerrar programa) '))
    def canalMais(self):
        if self.ligado:
            if self.canalAtual == self.canalMax:
                self.canalAtual = self.canalMin
            else:
                self.canalAtual += 1
    def canalMenos(self):
        if self.ligado:
            if self.canalAtual == self.canalMin:
                self.canalAtual = self.canalMax
            else:
                self.canalAtual -= 1
    def volMais(self):
        if self.ligado:
            if self.volumeAtual != self.volMax:
                self.volumeAtual += 1
    def volMenos(self):
        if self.ligado:
            if self.volumeAtual != self.volMin:
                self.volumeAtual -= 1
    def mostrarTV(self):
        print('TV ligada')
        self.comando = str(input(f'< CH{self.canalAtual} >  - VOL{self.volumeAtual} + '))
c1 = controleRemoto()
c1.controle()
while c1.comando != '0':
    c1.mostrarTV()
    match c1.comando:
        case '>':
            c1.canalMais()

        case '<':
            c1.canalMenos()

        case '+':
            c1.volMais()

        case '-':
            c1.volMenos()

        case '@':
            c1.desligar()
            