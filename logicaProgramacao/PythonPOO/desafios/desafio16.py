class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentar(self):
        print(f'Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo')

c1 = Funcionario('Luiz', 'Administração', 'Diretor')
c1.apresentar()